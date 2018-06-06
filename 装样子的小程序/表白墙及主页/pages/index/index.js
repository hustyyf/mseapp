Page({
    data: {
        tmd:1.00,
        hidd:0,
        list: [
            {
                id: 'house',
                name: '公用房',
                open: false,
                pages: ['view', 'scroll-view', 'swiper']
            }, {
                id: 'heart',
                name: '表白墙',
                open: false,
                pages: ['text', 'icon', 'progress']
            }, {
                id: 'message',
                name: '发短信',
                open: false,
                pages: ['button', 'checkbox', 'form', 'input', 'label', 'picker', 'radio', 'slider', 'switch', 'textarea']
            }
        ]
    },
    kindToggle: function (e) {
        var id = e.currentTarget.id, list = this.data.list;
        for (var i = 0, len = list.length; i < len; ++i) {
            if (list[i].id == id) {
                list[i].open = !list[i].open
            } else {
                list[i].open = false
            }
        }
        this.setData({
            list: list
        });
    },
    onReady: function (options) {
      var tmdd=1.00;
      var that=this;
      var x=setTimeout(
        function(){
          var int = setInterval(
            function () {
              if (tmdd > 0) {
                tmdd = tmdd - 0.01;
                that.setData({
                  tmd: tmdd,
                })
              } else {
                that.setData({
                  hidd:1,
                });
                clearInterval(int)
              }
            },
            10
          );
        },
        3000);
        
    },
})

