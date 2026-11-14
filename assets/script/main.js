document.addEventListener("DOMContentLoaded", function () {

    // Navbar: collapse toggle and dropdowns (styles in _sass/_foundation.scss)
    const toggler = document.querySelector('.navbar-toggler');
    const collapse = toggler && document.getElementById(toggler.getAttribute('aria-controls'));
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const isCollapsedNav = function () {
        return toggler && getComputedStyle(toggler).display !== 'none';
    };

    // Slide an element open or closed: height (plus padding and opacity for
    // dropdown menus) animates between zero and the natural size
    const slide = function (el, open) {
        if (reduceMotion.matches || !el.animate) {
            el.classList.toggle('show', open);
            return;
        }
        el.classList.add('show', 'sliding');
        const style = getComputedStyle(el);
        const shown = { height: el.offsetHeight + 'px' };
        const hidden = { height: '0px' };
        if (el.classList.contains('dropdown-menu')) {
            Object.assign(shown, { paddingTop: style.paddingTop, paddingBottom: style.paddingBottom, opacity: 1 });
            Object.assign(hidden, { paddingTop: '0px', paddingBottom: '0px', opacity: 0 });
        }
        const anim = el.animate(open ? [hidden, shown] : [shown, hidden], { duration: 280, easing: 'ease' });
        anim.onfinish = anim.oncancel = function () {
            el.classList.remove('sliding');
            el.classList.toggle('show', open);
        };
    };

    if (collapse) {
        toggler.addEventListener('click', function () {
            if (collapse.classList.contains('sliding')) return;
            const open = toggler.getAttribute('aria-expanded') !== 'true';
            toggler.setAttribute('aria-expanded', open);
            slide(collapse, open);
        });
    }

    // Dropdown menus: click to open; Escape, outside click or Tab away closes.
    // In the collapsed (mobile) navbar they slide; on desktop CSS fades them in.
    const toggles = document.querySelectorAll('.dropdown-toggle');

    const setMenu = function (t, open) {
        const menu = t.nextElementSibling;
        if (menu.classList.contains('show') === open && !menu.classList.contains('sliding')) return;
        t.classList.toggle('show', open);
        t.setAttribute('aria-expanded', open);
        if (isCollapsedNav()) {
            slide(menu, open);
        } else {
            menu.classList.toggle('show', open);
        }
    };

    const closeMenus = function (except) {
        toggles.forEach(function (t) {
            if (t !== except && t.classList.contains('show')) setMenu(t, false);
        });
    };

    toggles.forEach(function (t) {
        const menu = t.nextElementSibling;

        t.addEventListener('click', function (e) {
            e.preventDefault();
            if (menu.classList.contains('sliding')) return;
            closeMenus(t);
            setMenu(t, !t.classList.contains('show'));
        });

        // Arrow keys move through the items, as with Bootstrap
        t.parentElement.addEventListener('keydown', function (e) {
            if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return;
            e.preventDefault();
            if (!menu.classList.contains('show')) t.click();
            const items = Array.from(menu.querySelectorAll('.dropdown-item'));
            const i = items.indexOf(document.activeElement);
            const next = e.key === 'ArrowDown' ? Math.min(i + 1, items.length - 1) : Math.max(i - 1, 0);
            items[i === -1 ? 0 : next].focus();
        });

        t.parentElement.addEventListener('focusout', function (e) {
            if (e.relatedTarget && !t.parentElement.contains(e.relatedTarget)) closeMenus();
        });
    });

    document.addEventListener('click', function (e) {
        if (!e.target.closest('.dropdown')) closeMenus();
    });

    document.addEventListener('keydown', function (e) {
        if (e.key !== 'Escape') return;
        const open = document.querySelector('.dropdown-toggle.show');
        if (open) {
            closeMenus();
            open.focus();
        }
    });

    // Let wide tables scroll inside the content column instead of widening the page
    document.querySelectorAll('main table').forEach(function (table) {
        if (table.parentElement.classList.contains('table-scroll') || table.closest('.table-responsive')) return;
        const wrap = document.createElement('div');
        wrap.className = 'table-scroll';
        table.parentNode.insertBefore(wrap, table);
        wrap.appendChild(table);
    });

    const searchField = document.getElementById('search-field');

    if (searchField) {
        // Focus the input when the search icon is clicked
        document.getElementById('search-btn').addEventListener('click', function () {
            searchField.focus();
        });

        // Filter the results as the visitor types
        searchField.addEventListener('input', function () {
            const query = this.value;
            const entryParent = document.getElementById('result-list');
            const entries = entryParent.querySelectorAll('li:not(#no-result)');
            let hasResult = false;
            const noResult = document.getElementById('no-result');

            if (query !== undefined && query !== '') {
                entries.forEach(function (entry) {
                    if (entry.textContent.toLowerCase().indexOf(query.toLowerCase()) === -1) {
                        entry.style.display = 'none';
                    } else {
                        hasResult = true;
                        entry.style.display = '';
                    }
                });

                if (hasResult) {
                    noResult.style.display = 'none';
                } else {
                    noResult.style.display = '';
                }
            }

            if (query !== '') {
                entryParent.style.display = 'block';
            } else {
                entryParent.style.display = 'none';
            }
        });

        const closeSearch = function () {
            const searchField = document.getElementById('search-field');
            searchField.value = '';
            searchField.dispatchEvent(new Event('input'));
        };

        // Close the search result when clicking outside
        document.body.addEventListener('click', function (e) {
            if (!document.getElementById('search-area').contains(e.target)) {
                closeSearch();
            }
        });

        document.addEventListener('keyup', function (e) {
            if (e.key === 'Escape') {
                closeSearch();
            }
        });

        // "/" focuses the search box, unless the visitor is already typing somewhere
        document.addEventListener('keydown', function (e) {
            if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return;
            const el = document.activeElement;
            if (el && (el.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName))) return;
            e.preventDefault();
            searchField.focus();
        });
    }

    // Control size of navbar on scrolling
    window.addEventListener('scroll', function () {
        const navbar = document.querySelector('.navbar');
        const main = document.querySelector('main');
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;

        if (scrollTop > 50) {
            navbar.classList.add('navbar-small');
            main.style.marginTop = '100px';
        } else {
            navbar.classList.remove('navbar-small');
            main.removeAttribute('style');
        }

        if (window.innerWidth > 768) {
            const elem = document.querySelector('aside ins.adsbygoogle');
            if (elem) {
                if (scrollTop > 0) {
                    elem.style.position = 'fixed';
                    elem.style.top = '20px';
                } else {
                    elem.style.position = 'relative';
                }
            }
        }
    });

});
