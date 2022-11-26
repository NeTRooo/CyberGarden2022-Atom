if(navigator.webkitGetUserMedia!=null) {
    var options = {
      video:true,
      audio:false
    };
    navigator.webkitGetUserMedia(options,
      function(stream) {
        var video = document.querySelector('video');
        // console.log(video.srcObject=stream);
        video.srcObject=stream;
      },
      function(e) {
        console.log("error happened");
      }
    );
}