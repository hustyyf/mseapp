var utils=require("../../utils/util.js")

Page({
  data: {
    roomIndex: 0,
    roomNum:["129","136","138","345"],
    list: [
      {
        id: 'view',
        name: '05-26',
        open: false,
        pages: ['8：00-10：00', '12：00-13：00','13：10-14：10','19：00-23：00']
      }, {
        id: 'content',
        name: '05-27',
        open: false,
        pages: ['text', 'icon', 'progress']
      }, {
        id: 'form',
        name: '05-28',
        open: false,
        pages: ['button', 'checkbox', 'form', 'input', 'label', 'picker', 'radio', 'slider', 'switch', 'textarea']
      }, {
        id: 'nav',
        name: '05-29',
        open: false,
        pages: ['navigator']
      }, {
        id: 'media',
        name: '05-30',
        open: false,
        pages: ['image', 'audio', 'video']
      }, {
        id: 'map',
        name: '05-31',
        pages: ['map']
      }, {
        id: 'canvas',
        name: '06-01',
        pages: ['canvas']
      }
    ]
  },

  onLoad: function (options) {
    // Do some initialize when page load.
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
  bindRoomChange: function (e) {
    this.setData({
      roomIndex: e.detail.value
    })
  },
})

