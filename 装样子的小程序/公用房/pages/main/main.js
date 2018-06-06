Page({
  data: {
    
  },
  onLoad: function () {
    console.log('onLoad')
    var that=this
    wx.request({
      url: 'http://localhost:81/polls/list',
      header:{
        'Content-Type':'application/json'
      },

      success: function(res){
        var jsonStr = res.data;
        jsonStr = jsonStr.replace(" ", "");
        if (typeof jsonStr != 'object') {
          jsonStr = jsonStr.replace(/\ufeff/g, "");//重点
          var jj = JSON.parse(jsonStr);
          res.data = jj;
        }
        that.setData({
          listData:res.data
        })
      }
    })
  }

})