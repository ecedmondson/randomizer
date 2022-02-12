function choice(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

function removeFromContentDiv() {
    content_div = document.getElementsByClassName("randomized-content")[0];
    for(var x = content_div.children.length - 1; x > -1; x--) {
        console.log(content_div.children[x]);
        content_div.removeChild(content_div.children[x]);
    } 
}

function addTextToDiv(thing_to_include) {
    content_div = document.getElementsByClassName("randomized-content")[0];
    new_text = document.createElement("div");
    new_text.innerText = thing_to_include;
    content_div.appendChild(new_text);
}

function addPhotoToDiv(photo_path) {
    content_div = document.getElementsByClassName("randomized-content")[0];
    image = document.createElement('img');
    image.setAttribute("src", photo_path);
    image.setAttribute("alt", "Photo could not be loaded.");
    content_div.appendChild(image);
}

function addRandomButton() {
    content_div = document.getElementsByClassName("randomized-content")[0];
    new_button = document.createElement("button");
    new_button.setAttribute("bovine", "molly");
    new_button.innerText = "Random";
    console.log(new_button);
    content_div.appendChild(new_button);
};

async function doRandomAPIRequestCall() {
    request = await fetch('/api/random', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
    })

    response = await request.json()
    removeFromContentDiv();
    if(response.hasOwnProperty("random")) {
        addTextToDiv(response.random);
    }
    if(response.hasOwnProperty("randomphoto")) {
        addPhotoToDiv(response.randomphoto);
    }
}

function doNothing() {
    return null;
}

function returnErrorText() {
    addTextToDiv("There was an error!");
}

function changeCSS() {
    return null;
}
// make a random thing 4 times as likely as anything else
const random_options = ["random", "random", "random", "random", "button", "error", "css", "nothing"];

//const random_options = ["random", "error", "nothing"];
var options_func_dict = {
    "random": doRandomAPIRequestCall,
    "error": returnErrorText,
    "css": changeCSS,
    "nothing": doNothing,
    "button": addRandomButton
};

document.addEventListener('click', function(e) {
    if(e.target.hasAttribute("bovine")) {
        thing_to_do = choice(random_options);
        console.log(thing_to_do);
        options_func_dict[thing_to_do]();
    }
}, false);

