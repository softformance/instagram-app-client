"use strict";

function initInstagramStream() {
    $(".fancybox").attr("rel", "gallery").fancybox({
        margin: [20, 20, 100, 20],
        autoHeight: true,
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

    marginBottom = marginBottom || 10;
    marginBottom = -activeImage.outerHeight() - marginBottom;
    activeImage.css("margin-bottom", marginBottom);
}

window.addEventListener('resize', function () {
    setTitleMargin()
});
document.addEventListener('DOMContentLoaded', initInstagramStream);
