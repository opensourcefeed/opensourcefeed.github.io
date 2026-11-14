document.addEventListener("DOMContentLoaded", function () {

    // Navbar: collapse toggle on small screens (styles in _sass/_foundation.scss)
    const toggler = document.querySelector('.navbar-toggler');
    const collapse = toggler && document.getElementById(toggler.getAttribute('aria-controls'));
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    if (collapse) {
        const setOpen = function (open) {
            toggler.setAttribute('aria-expanded', open);
            if (reduceMotion.matches) {
                collapse.classList.toggle('show', open);
                return;
            }
            // Animate the height between 0 and the content height, then hand back to CSS
            const from = open ? 0 : collapse.scrollHeight;
            collapse.classList.add('show');
            const to = open ? collapse.scrollHeight : 0;
            collapse.classList.add('collapsing');
            collapse.style.height = from + 'px';
            collapse.offsetHeight; // apply the start height before transitioning
            collapse.style.height = to + 'px';
            collapse.addEventListener('transitionend', function done() {
                collapse.removeEventListener('transitionend', done);
                collapse.classList.remove('collapsing');
                collapse.classList.toggle('show', open);
                collapse.style.height = '';
            });
        };

        toggler.addEventListener('click', function () {
            if (collapse.classList.contains('collapsing')) return;
            setOpen(toggler.getAttribute('aria-expanded') !== 'true');
        });
    }

    // Navbar: dropdown menus (click to open; Escape, outside click or Tab away closes)
    const toggles = document.querySelectorAll('.dropdown-toggle');

    const closeMenus = function (except) {
        toggles.forEach(function (t) {
            if (t === except) return;
            t.classList.remove('show');
            t.setAttribute('aria-expanded', 'false');
            t.nextElementSibling.classList.remove('show');
        });
    };

    toggles.forEach(function (t) {
        const menu = t.nextElementSibling;

        t.addEventListener('click', function (e) {
            e.preventDefault();
            closeMenus(t);
            const open = !menu.classList.contains('show');
            t.classList.toggle('show', open);
            t.setAttribute('aria-expanded', open);
            menu.classList.toggle('show', open);
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

        // Filter the results on keyup
        document.getElementById('search-field').addEventListener('keyup', function () {
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

            if (hasResult) {
                entryParent.style.width = (this.offsetWidth - 1) + 'px';
                entryParent.style.marginLeft = document.getElementById('search-btn').offsetWidth + 'px';
                entryParent.style.display = 'block';
            } else {
                entryParent.style.display = 'none';
            }
        });

        const closeSearch = function () {
            const searchField = document.getElementById('search-field');
            searchField.value = '';
            searchField.dispatchEvent(new Event('keyup'));
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
