Page({
    data: {
        focus: false
    },
    bindTextAreaBlur: function (e) {
        console.log(e.detail.value)
    },
    bindSubmitTap: function(e){
      wx.showToast({
        title: '成功，等待审核',
        icon:'success',
      })
    }
})
