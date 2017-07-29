"use strict";

function initInstagramStream() {
    $(".fancybox").attr("rel", "gallery").fancybox({
        arrows: false,
        beforeLoad: function () {
            divAsTitle(this);
        },
        afterShow: function () {
            setTitleMargin();
            bindPhotoAsLink(this);
        }
    });
}

function divAsTitle(self) {
    var el,
        id = $(self.element).data("title-id");

    if (id) {
        el = $("#" + id);

        if (el.length) {
            self.title = el.html();
        }
    }
}

function bindPhotoAsLink(self) {
    $(".fancybox-image").click(function () {
        window.open(self.element.data("link"), '_blank');
    });
}

function setTitleMargin(marginBottom) {
    var activeImage = $($(".fancybox-opened .fancybox-title")[0]);

    marginBottom = marginBottom || 5;
    marginBottom = -activeImage.outerHeight() - marginBottom;
    activeImage.css("margin-bottom", marginBottom);
}

document.addEventListener('DOMContentLoaded', initInstagramStream);
