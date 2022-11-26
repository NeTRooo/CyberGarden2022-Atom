        function getRandomInt(max) {
          return Math.floor(Math.random() * max);
        }

        function drawLine( ctx, x1, y1, x2, y2 ) {
            ctx.beginPath();
            ctx.moveTo( x1, y1 );
            ctx.lineTo( x2, y2 );
            ctx.stroke();
        }

        function drawText( ctx, x1, y1, text){
            ctx.fillStyle = "##E0FFFF	";
            ctx.strokeStyle = "##E0FFFF	";
            ctx.font = 'bold 15px sans-serif';
            ctx.fillText(text, x1, y1);

        }

        let output = null;
        let model = null;

        async function setupWebcam() {
            return new Promise( ( resolve, reject ) => {
                const webcamElement = document.getElementById( "webcam" );
                const navigatorAny = navigator;
                navigator.getUserMedia = navigator.getUserMedia ||
                navigatorAny.webkitGetUserMedia || navigatorAny.mozGetUserMedia ||
                navigatorAny.msGetUserMedia;
                if( navigator.getUserMedia ) {
                    navigator.getUserMedia( { video: true },
                        stream => {
                            webcamElement.srcObject = stream;
                            webcamElement.addEventListener( "loadeddata", resolve, false );
                        },
                    error => reject());
                }
                else {
                    reject();
                }
            });
        }

        let i = 0;
        let old_count_people = 0;
        let new_count_people = 0;


        function isEmpty(obj) {
            for(var prop in obj) {
                if(obj.hasOwnProperty(prop))
                    return false;
            }

            return true;
        }

        percentage = []

        function generate_percentage(old_count_people, new_count_people) {
          if (old_count_people != new_count_people){
            percentage = []
            for (let i = 0; i < new_count_people; i++){
              perc = getRandomInt(100);
              percentage.push(perc);
            }
            for (let i; i < 10000; i++){
              text = 'Junior-разработчик на ' + getRandomInt(100) + '%';
              console.log(i);
              drawText( output, x1, y1, text);
            }
          }
        }

        async function trackFace() {
            const video = document.getElementById( "webcam" );
            const faces = await model.estimateFaces( {
                input: video,
                returnTensors: false,
                flipHorizontal: false,
            });
            output.drawImage(
                video,
                0, 0, video.width, video.height,
                0, 0, video.width, video.height
            );

            if (isEmpty(faces) === true) {
              new_count_people = 0;
              old_count_people = -1;
            } else {
              new_count_people = faces.length;
            }
            let cnt = 0;
            faces.forEach( face => {
                cnt = cnt + 1;
                console.log(cnt);

                // Draw the bounding box
                const x1 = face.boundingBox.topLeft[ 0 ];
                const y1 = face.boundingBox.topLeft[ 1 ];
                const x2 = face.boundingBox.bottomRight[ 0 ];
                const y2 = face.boundingBox.bottomRight[ 1 ];
                const bWidth = x2 - x1;
                const bHeight = y2 - y1;
                drawLine( output, x1, y1, x2, y1 );
                drawLine( output, x2, y1, x2, y2 );
                drawLine( output, x1, y2, x2, y2 );
                drawLine( output, x1, y1, x1, y2 );

                generate_percentage(old_count_people, new_count_people);

                text = 'Junior-разработчик на ' + percentage[cnt-1] + '%';
                drawText( output, x1, y1-5, text);
                text1 = '(' + Math.round(x1) + ', ' + Math.round(y1) + '), (' + Math.round(x2) + ',' + Math.round(y2) + ')'
                drawText( output, x1, y2-5, text1);

                old_count_people = faces.length;
            });

            requestAnimationFrame( trackFace );
        }

        (async () => {
            await setupWebcam();
            const video = document.getElementById( "webcam" );
            video.play();
            let videoWidth = video.videoWidth;
            let videoHeight = video.videoHeight;
            video.width = videoWidth;
            video.height = videoHeight;

            let canvas = document.getElementById( "output" );
            canvas.width = video.width;
            canvas.height = video.height;

            output = canvas.getContext( "2d" );
            //output.translate( canvas.width, 0 );
            //output.scale( -1, 1 ); // Mirror cam
            output.fillStyle = "#00ff00";
            output.strokeStyle = "#ff0000";
            output.lineWidth = 2;

            // Load Face Landmarks Detection
            model = await faceLandmarksDetection.load(
                faceLandmarksDetection.SupportedPackages.mediapipeFacemesh
            );


            trackFace();
        })();