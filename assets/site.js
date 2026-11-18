/* Elite Immigration concept: menu, settlement tool, enquiry form, WeChat copy, lazy map. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);

  // ---- menu
  const btn = $('.menu-btn');
  const menu = $('#menu');
  if (btn && menu) {
    const head = $('.head');
    const setMenu = (open) => {
      if (open) menu.style.setProperty('--menu-top', `${Math.round(head.getBoundingClientRect().bottom)}px`);
      btn.setAttribute('aria-expanded', String(open));
      menu.hidden = !open;
      document.body.classList.toggle('menu-open', open);
    };
    btn.addEventListener('click', (e) => { e.preventDefault(); setMenu(btn.getAttribute('aria-expanded') !== 'true'); });
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); btn.focus(); } });
    window.addEventListener('resize', () => { if (!menu.hidden && window.innerWidth > 980) setMenu(false); });
  }

  // ---- copy WeChat ID
  const toast = $('.toast');
  document.addEventListener('click', async (e) => {
    const b = e.target.closest('[data-copy]');
    if (!b) return;
    try { await navigator.clipboard.writeText(b.dataset.copy); } catch (err) { /* clipboard blocked: still show the ID */ }
    if (toast) {
      toast.textContent = `${b.dataset.done}: ${b.dataset.copy}`;
      toast.classList.add('on');
      clearTimeout(toast.t);
      toast.t = setTimeout(() => toast.classList.remove('on'), 2600);
    }
  });

  // ---- settlement tool
  const tool = $('#tool');
  const T = $('#tool-text') ? JSON.parse($('#tool-text').textContent) : null;
  if (tool && T) {
    const route = $('#t-route'); const start = $('#t-start'); const pay = $('#t-pay'); const brit = $('#t-brit');
    const fmt = new Intl.DateTimeFormat(T.locale, T.locale === 'en-GB' ? { day: 'numeric', month: 'short', year: 'numeric' } : { day: '2-digit', month: '2-digit', year: 'numeric' });
    const iso = (d) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
    const addYears = (d, n) => {
      const r = new Date(d.getFullYear() + n, d.getMonth(), d.getDate());
      if (r.getMonth() !== d.getMonth()) r.setDate(0); // 29 Feb -> 28 Feb
      return r;
    };
    const addDays = (d, n) => new Date(d.getFullYear(), d.getMonth(), d.getDate() + n);
    const YEARS = { bno: 5, partner: 5, skilled: 5, innovator: 3, long: 10 };

    // a sensible first example: three years ago today
    const today = new Date();
    start.value = iso(addYears(today, -3));
    start.max = iso(today);

    const fill = (id, v) => { $(id).innerHTML = v; };
    const run = () => {
      const r = route.value;
      $('.f-pay').hidden = r !== 'skilled';
      $('.f-brit').hidden = r !== 'partner';
      const s = start.value ? new Date(`${start.value}T12:00:00`) : null;
      if (!s || Number.isNaN(s.getTime())) {
        fill('#t-d0', T.pick); fill('#t-d1', '—'); fill('#t-d2', '—'); fill('#t-n1', ''); fill('#t-n2', ''); $('#t-change').innerHTML = '';
        return;
      }
      const y = YEARS[r];
      const ilr = addYears(s, y);
      const isBrit = r === 'partner' && $('#t-brit').value === 'yes';
      const cit = isBrit ? ilr : addYears(ilr, 1);
      fill('#t-d0', fmt.format(s));
      fill('#t-d1', fmt.format(ilr));
      fill('#t-n1', `${T.years.replace('{n}', y)} · ${T.apply.replace('{d}', fmt.format(addDays(ilr, -28)))}`);
      fill('#t-d2', fmt.format(cit));
      fill('#t-n2', isBrit ? T.withIlr : T.afterIlr);

      let msg = T.c[r];
      if (r === 'skilled') {
        const p = pay.value;
        msg = T.c[`skilled_${p}`];
        if (p === 'low') msg = msg.replace('{d}', fmt.format(addYears(s, 10)));
        if (p === 'high') msg = msg.replace('{d}', fmt.format(addYears(s, 3)));
      }
      $('#t-change').innerHTML = `<p><span class="tag">${T.plan}</span>${msg}</p>`;
      const sum = `${route.options[route.selectedIndex].text}: ${fmt.format(s)} → ILR ${fmt.format(ilr)}`;
      const hid = $('#f-dates');
      if (hid) hid.value = sum;
    };
    [route, start, pay, brit].forEach((el) => el.addEventListener('input', run));
    [route, pay, brit].forEach((el) => el.addEventListener('change', run));
    tool.addEventListener('submit', (e) => e.preventDefault());
    run();
  }

  // ---- enquiry form: opens a pre-filled email
  const form = $('#enquiry');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const f = new FormData(form);
      const err = $('.f-err', form);
      if (!String(f.get('name')).trim() || !String(f.get('phone')).trim()) {
        err.hidden = false;
        (String(f.get('name')).trim() ? form.phone : form.name).focus();
        return;
      }
      err.hidden = true;
      const lines = [
        `${f.get('name')}`,
        `${f.get('phone')}`,
        f.get('email') ? `${f.get('email')}` : '',
        `${f.get('topic')}`,
        f.get('dates') ? `${f.get('dates')}` : '',
        '',
        `${f.get('msg')}`,
      ].filter((l, i, a) => l !== '' || i === a.length - 2);
      const subject = `${form.dataset.subject}: ${f.get('topic')}`;
      window.location.href = `mailto:${form.dataset.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;
    });
  }

  // ---- map: load MapLibre only when the map comes near the screen
  const box = $('[data-map]');
  if (box && 'IntersectionObserver' in window) {
    const root = document.querySelector('link[rel="stylesheet"][href*="site.css"]').getAttribute('href').replace(/assets\/site\.css.*$/, '');
    const load = (src) => new Promise((res, rej) => { const s = document.createElement('script'); s.src = src; s.onload = res; s.onerror = rej; document.head.appendChild(s); });
    const io = new IntersectionObserver(async (entries) => {
      if (!entries.some((en) => en.isIntersecting)) return;
      io.disconnect();
      try {
        const css = document.createElement('link');
        css.rel = 'stylesheet'; css.href = `${root}assets/vendor/maplibre/maplibre-gl.css`;
        document.head.appendChild(css);
        await load(`${root}assets/vendor/maplibre/maplibre-gl.js`);
        await load(`${root}assets/map.js?v=1`);
        window.eiMap(box);
      } catch (err) { /* keep the sketch map */ }
    }, { rootMargin: '400px' });
    io.observe(box);
  }
})();
