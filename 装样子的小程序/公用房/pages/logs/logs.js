//logs.js
const util = require('../../utils/util.js')

Page({
  data: {
  roomNum:[ '129','136','138','345'],
  index:0
  },
  
onLoad:function () {
 
  var wholedate = util.formatTime(new Date());

  var today = new Date();
  
  var day = today.getDate();

  this.setData({
    today:day,
    date: wholedate.slice(0,10),
    time1:wholedate.slice(11,-3),
    time2: wholedate.slice(11, -3)
  });
},
  
switchChange: function(e){
    console.log(e.detail.value)
    
},

bindDateChange: function (e) {
  this.setData({
    date: e.detail.value
  })
},
bindTimeChange1: function (e) {
  this.setData({
    time1: e.detail.value
  })
},
  bindTimeChange2: function (e) {
    this.setData({
      time2: e.detail.value
    })
  },


bindRoomChange: function(e){
    this.setData({
      index:e.detail.value
    })
},
})