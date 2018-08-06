$(function () {
    // Custom code to handle nested navigation menu
    $('.dropdown-menu a.dropdown-toggle').on('click', function () {
        if (!$(this).next().hasClass('show')) {
            $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
        }
        var $subMenu = $(this).next(".dropdown-menu");
        $subMenu.toggleClass('show');


        $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function () {
            $('.dropdown-submenu .show').removeClass("show");
        });


        return false;
    });

    // Filter the results on keyup
    $('#search-field').on('keyup', function () {

        var query = $(this).val();
        var entryParent = $('#result-list');
        var entries = $(entryParent).find('li').not('#no-result');
        var hasResult = false;
        var noResult = $('#no-result');

        if (query != undefined && query != '') {
            $(entries).each(function () {
                if ($(this).text().toLowerCase().indexOf(query.toLowerCase()) == -1) {
                    $(this).hide();
                } else {
                    hasResult = true;
                    $(this).show();
                }
            });
            if (hasResult) {
                $(noResult).hide();
            } else {
                $(noResult.show());
                hasResult = true;
            }
        }

        if (hasResult) {
            $(entryParent).width($(this).outerWidth())
            .css('left', $('#search-btn').parent().width())
            .show();
        } else {
            $(entryParent).hide();
        }
    });

    // Control size of navbar on scrolling
    $(window).scroll(function () {
        if ($(document).scrollTop() > 0) {
          $('.navbar').addClass('navbar-small');
      }
      else {
          $('.navbar').removeClass('navbar-small');
      }
  });
});