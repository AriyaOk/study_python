const like = function (element, post_id) {
    let api_url = "/b/post/" + post_id + "/like/";

    fetch(api_url, {
        method: "POST",
    }).then(
        resp => {
            resp.json().then(
                resp_payload => {
                    if (resp_payload.ok) {
                        element.textContent = resp_payload.nr_likes;
                        if (resp_payload.is_like){element.className = "likes";}
                        else{element.className = "nolikes"}

                    } else {
                        console.log(JSON.stringify(resp_payload));
                    }
                }
            );
        }
    );
}