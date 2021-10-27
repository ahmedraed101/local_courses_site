const coursename= document.querySelector(".coursename").dataset.name;
const video = document.querySelector("#video");
const source = document.querySelector("#source");
const videoCourses = document.querySelectorAll(".videoCourse");
const videoTitle = document.querySelectorAll("h2")[0]

videoCourses.forEach(function(element){
    element.addEventListener("click", function(){
        source.setAttribute('src', `./../static/courses/${coursename}/${this.dataset.video}/${this.dataset.video}.mp4`)
        video.appendChild(source);
        video.load()
        videoTitle.innerText = this.dataset.video
        video.play()
    })
})

// const videoElem = document.querySelector("#video")
// videoCourses.forEach(function (element) {
//     element.addEventListener("click" ,function(){
//         console.log(coursename)
//         console.log(this.dataset.video)
//         videoElem.src = `./../static/courses/${coursename}/${this.dataset.video}/${this.dataset.video}.mp4`
        
//     })
// })