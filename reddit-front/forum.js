"use strict";

const testURL = "http://secure-reddit.herokuapp.com/simple"
const LeviURL = "https://time-radish.glitch.me/posts"

class DataLoader {
    constructor(URL){
        this.posts = [];
        this.url = URL;
    }

    loadData(){
    let myRequest = new XMLHttpRequest();
    myRequest.open("GET", this.url, true);
    // myRequest.setRequestHeader("Content-Type", "application/json");
    myRequest.setRequestHeader("Accept", "application/json");
    myRequest.send();
    myRequest.onload = function () {
        this.posts = JSON.parse(myRequest.responseText);
        console.log(this.posts);
        }
    }
}

class Renderer {
    constructor(){
    }

    timeStampToDate(timeStamp){
        let date = new Date(timeStamp * 1000);
        let hours = date.getHours();
        let minutes = "0" + date.getMinutes();
        return hours + ":" + minutes.substr(-2);
    }

    renderPost(htmlElement, postData){
        let PostUrl = "";
        let newTag = document.createElement('div'); /* lebeg ez a div a semmiben */
        newTag.id = "post" + postData['id'];
        newTag.className = "post"

        console.log(postData)

        if ("url" in postData){
            postUrl = postData['url']
        } else if ("href" in postData) {
            postUrl = postData['href']
        }

        let newData = `
        <div id = "post_id" class = "post">
            <div class = "feedback">
                <div class = "upvote">▲</div>
                <div class = "score">${postData["score"]}</div>
                <div class = "downvote">▼</div>
            </div>
            <div class = "postBody">
                <div class = "topic">${postData["title"]}</div>
                <div class = "url"><a href=${postUrl}>link</a></div>
                <div class = "postinfo">${this.timeStampToDate(postData["timestamp"])} posted by: ${postData["owner"]}</div>
            </div>
        </div>
    </div>`;

    newTag.innerHTML = newData; /* a lebegő div-et bebasszuk a html-ben lévő div helyére */

    htmlElement.appendChild(newTag);

    }
}

let targetHtmlElement = document.querySelector("#content")

let myRenderer = new Renderer

let myDataLoader = new DataLoader(LeviURL);

myDataLoader.loadData();

setTimeout(myDataLoader.posts.forEach(element => {myRenderer.renderPost(targetHtmlElement, element)}), 2000);

myRenderer.renderPost(targetHtmlElement,"");

console.log(targetHtmlElement)




