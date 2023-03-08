function fqa(){
    /* hidden fqa column1-1 */
const column1Title = document.querySelector('.column1_title');
const column1Description = document.querySelector('.column1_description');

column1Title.addEventListener('click', () => {
    column1Description.classList.toggle('hidden');
});

var isClosed = true;
function showfqa() {
  if (isClosed == true) {
    document.getElementById("fqa_icon").className = "fa-solid fa-sort-up";
    isClosed = false;
  } else {
    document.getElementById("fqa_icon").className = "fa-solid fa-sort-up rotation";
    isClosed = true;
  }

}
/* hidden fqa column1-2 */
const column1Title1 = document.querySelector('.column1_title1');
const column1Description1 = document.querySelector('.column1_description1');

column1Title1.addEventListener('click', () => {
    column1Description1.classList.toggle('hidden');
});

var isClosed = true;
function showfqa12() {
  if (isClosed == true) {
    document.getElementById("fqa_icon 12").className = "fa-solid fa-sort-up";
    isClosed = false;
  } else {
    document.getElementById("fqa_icon 12").className = "fa-solid fa-sort-up rotation";
    isClosed = true;
  }

}

/* hidden fqa column1-3 */
const column1Title2 = document.querySelector('.column1_title2');
const column1Description2 = document.querySelector('.column1_description2');

column1Title2.addEventListener('click', () => {
    column1Description2.classList.toggle('hidden');
});

var isClosed = true;
function showfqa13() {
  if (isClosed == true) {
    document.getElementById("fqa_icon 13").className = "fa-solid fa-sort-up";
    isClosed = false;
  } else {
    document.getElementById("fqa_icon 13").className = "fa-solid fa-sort-up rotation";
    isClosed = true;
  }

}

/* hidden fqa column2-1 */
const column2Title = document.querySelector('.column2_title');
const column2Description = document.querySelector('.column2_description');

column2Title.addEventListener('click', () => {
    column2Description.classList.toggle('hidden');
});

var isClosed = true;







function showfqa2() {
  if (isClosed == true) {
    document.getElementById("fqa_icon 2").className = "fa-solid fa-sort-up";
    isClosed = false;
  } else {
    document.getElementById("fqa_icon 2").className = "fa-solid fa-sort-up rotation";
    isClosed = true;
  }

}

/* hidden fqa column2-2 */
const column2Title2 = document.querySelector('.column2_title2');
const column2Description2 = document.querySelector('.column2_description2');

column2Title2.addEventListener('click', () => {
    column2Description2.classList.toggle('hidden');
});

var isClosed = true;
function showfqa22() {
  if (isClosed == true) {
    document.getElementById("fqa_icon 22").className = "fa-solid fa-sort-up";
    isClosed = false;
  } else {
    document.getElementById("fqa_icon 22").className = "fa-solid fa-sort-up rotation";
    isClosed = true;
  }

}
/* hidden fqa column2-3 */
const column2Title3 = document.querySelector('.column2_title3');
const column2Description3 = document.querySelector('.column2_description3');

column2Title3.addEventListener('click', () => {
    column2Description3.classList.toggle('hidden');
});

var isClosed = true;
function showfqa23() {
  if (isClosed == true) {
    document.getElementById("fqa_icon 23").className = "fa-solid fa-sort-up";
    isClosed = false;
  } else {
    document.getElementById("fqa_icon 23").className = "fa-solid fa-sort-up rotation";
    isClosed = true;
  }

}
}
// show, hide modal proflie
function showModalprofile() {
  var modal = document.querySelector('.modal_account');
  modal.style.display = 'flex';
}

function hideModalprofile() {
  var modal = document.querySelector('.modal_account');
  modal.style.display = 'none';
}


function gettimeline(){
               let gettimeline = async () => {
            let historydata = await axios.get("/api/v1/timeline/");
            let data = historydata.data
                timeline(data);
        }
        gettimeline();
        let myInterval = setInterval(() => {
         gettimeline();

            }, 30000);
}


function timeline(data) {
	var timeline = document.getElementById('timeline')
	document.getElementById('timeline').innerHTML = ''

	for (var i = 0; i < 20; i++) {

		username = data[i]["history_membername"]
		usercoins = data[i]["history_amount"]
		checkwithdraw = data[i]["history_network"]
		type = data[i]["history_type"]
		time = moment(data[i]["history_timecreated"]).startOf('minute').fromNow()
		avatar =  data[i]["history_member_avatar"]

			if (avatar == null || avatar == "") {
				var row = `<div class="row_item">
                            <div class="item_avatar">
                                    <img src="https://eu.ui-avatars.com/api/?background=random&color=fff&name=${data[i]["history_membername"]}" alt="" %}>
                            </div>
                            <div class="item_info">
                                <div class="info_lead">
                                    <div class="lead_network">${data[i]["history_network"].toUpperCase()}</div>
                                    <div class="lead_time">${time}</div>
                                </div>
                                <div class="info_offer">
                                    <div class="offer_text">
                                        <div class="text_nameoff">${data[i]["history_offername"]}</div>
                                        <div class="text_user">${username}</div>
                                    </div>
                                    <div class="offer_poin">${usercoins}</div>
                                </div>
                            </div>
                        </div>
`

				document.getElementById('timeline').innerHTML += row

			}else {
			var row = `<div class="row_item">
                            <div class="item_avatar">
                                    <img src="${avatar}" alt="" %}>
                            </div>
                            <div class="item_info">
                                <div class="info_lead">
                                    <div class="lead_network">${data[i]["history_network"].toUpperCase()}</div>
                                    <div class="lead_time">${time}</div>
                                </div>
                                <div class="info_offer">
                                    <div class="offer_text">
                                        <div class="text_nameoff">${data[i]["history_offername"]}</div>
                                        <div class="text_user">${username}</div>
                                    </div>
                                    <div class="offer_poin">${usercoins}</div>
                                </div>
                            </div>
                        </div>`

				document.getElementById('timeline').innerHTML += row

			}
	}

}


function animateHomeStats() {
    const totalAccStatEls = document.querySelectorAll("#totalAccStat");
    const totalStatEls = document.querySelectorAll("#usdEarnedStat");
    const dailyStatEls = document.querySelectorAll("#usdDailyStat");
    const payoutStatEls = document.querySelectorAll("#payoutStat");
    const users = "1235480";
    const averageUser = users / 1;
    for (let el of totalAccStatEls) {
        let numAnimTotal = new CountUp(el, 0, averageUser, 0, 0);
        if (!numAnimTotal.error) {
            numAnimTotal.start();
        }
    }

    const coins = "543352";
    const dollarsEarned = coins / 10;
    for (let el of totalStatEls) {
        let numAnimTotal = new CountUp(el, 0, dollarsEarned, 2, 4);
        if (!numAnimTotal.error) {
            numAnimTotal.start();
        }
    }

    const averageCoins = "434348";
    const averageEarned = averageCoins / 1;
    for (let el of dailyStatEls) {
        let numAnimDaily = new CountUp(el, 0, averageEarned, 0, 0);
        if (!numAnimDaily.error) {
            numAnimDaily.start();
        }
    }

    const averagePayout = "32178";
    const averagePay = averagePayout / 1;
    for (let el of payoutStatEls) {
        let numAnimDaily = new CountUp(el, 0, averagePay, 0, 0);
        if (!numAnimDaily.error) {
            numAnimDaily.start();
        }
    }
};


function modalwall(data, userid) {

	var modal = document.getElementById("WallModal");


	// Get the button that opens the modal
	var btnwall = document.getElementById("btnwall");

	// Get the <span> element that closes the modal
	var close = document.getElementById("closeModal");

	switch (data) {

		case "AdgateMedia":
			document.getElementById("iframe").innerHTML = ` <iframe  src="https://wall.adgaterewards.com/oaecqQ/${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Lootably":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://wall.lootably.com/?placementID=cl0ghjmbu04td012p667j8qid&sid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Offertoro":
			document.getElementById("iframe").innerHTML = `<iframe src="https://www.offertoro.com/ifr/show/23202/${userid}/14775"  style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Hangmyads":
			document.getElementById("iframe").innerHTML = `<iframe src="https://offerwall.hangmyads.com/offerwall.php?pubid=4853&subid=${userid}&curr=coins&percent=400" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Monlix":
			document.getElementById("iframe").innerHTML = `<iframe src="https://offers.monlix.com/?appid=1915&userid=${userid}" style="width:100%; height:100%; border:0; padding:0; margin:0;" scrolling="yes" frameborder="0";border-radius: 10px  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;

		case "Adgem":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://api.adgem.com/v1/wall?appid=16142&playerid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " >Your browser doesn't support iframes</iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Ayetstudio":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://www.ayetstudios.com/offers/web_offerwall/11096?external_identifier=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Notik":
			document.getElementById("iframe").innerHTML = `<iframe src='https://notik.me/coins?api_key=VUZeagwx7nqf8u4K1YaX0o95TkkVYoe7&pub_id=gnqI&user_id=${userid}'
		               style="width: 100%; height: 100%; border: none ;border-radius: 10px ";></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Cpalead":
			document.getElementById("iframe").innerHTML = `<iframe src="https://fastsvr.com/list/491571&subid=${userid} " style="width: 100%; height: 100%; border: none ;border-radius: 10px "; ></iframe>`;
			document.body.style.overflow = "hidden";
			break;

		case "Admantum":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://www.admantum.com/offers?appid=23264&uid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Admantium":
			document.getElementById("iframe").innerHTML = ` <iframe  src="https://offerwall.admantium.net?offerwall=a6a58aa0-2f63-11ed-8d37-03516a247812&user_id=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Timewall":
			document.getElementById("iframe").innerHTML = `<iframe src="https://timewall.io/users/login?oid=4e703e9d6826477a&uid=${userid}"   style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "CpxResearch":
			document.getElementById("iframe").innerHTML = `<iframe src="https://offers.cpx-research.com/index.php?app_id=17106&ext_user_id=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Bitlabs":
			document.getElementById("iframe").innerHTML = `<iframe src="https://web.bitlabs.ai/?token=18537c9a-4a49-4a4f-88e6-371f44af9310&uid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Wannads":
			document.getElementById("iframe").innerHTML = `<iframe src="https://wall.wannads.com/wall?apiKey=63a9bbb7e8d20454825288&userId=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Revenue":
			document.getElementById("iframe").innerHTML = `<iframe src="https://publishers.revenueuniverse.com/wallresp/508/offers?uid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Mmwall":
			document.getElementById("iframe").innerHTML = `<iframe src="https://wall.make-money.top/?p=195&u=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
	}

	// When the user clicks on the button, open the modal
	modal.style.display = "block";

	// When the user clicks on <span> (x), close the modal
	close.onclick = function() {
		modal.style.display = "none";
		document.body.style.overflow = "visible";

	};

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {

		if (event.target == modal) {
			modal.style.display = "none";
			document.body.style.overflow = "visible";
		}
	}
}



function modalwall(data, userid) {

	var modal = document.getElementById("WallModal");


	// Get the button that opens the modal
	var btnwall = document.getElementById("btnwall");

	// Get the <span> element that closes the modal
	var close = document.getElementById("closeModal");

	switch (data) {

		case "AdgateMedia":
			document.getElementById("iframe").innerHTML = ` <iframe  src="https://wall.adgaterewards.com/oaecqQ/${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Lootably":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://wall.lootably.com/?placementID=cl0ghjmbu04td012p667j8qid&sid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Offertoro":
			document.getElementById("iframe").innerHTML = `<iframe src="https://www.offertoro.com/ifr/show/23202/${userid}/14775"  style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Hangmyads":
			document.getElementById("iframe").innerHTML = `<iframe src="https://offerwall.hangmyads.com/offerwall.php?pubid=4853&subid=${userid}&curr=coins&percent=400" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Monlix":
			document.getElementById("iframe").innerHTML = `<iframe src="https://offers.monlix.com/?appid=1915&userid=${userid}" style="width:100%; height:100%; border:0; padding:0; margin:0;" scrolling="yes" frameborder="0";border-radius: 10px  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;

		case "Adgem":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://api.adgem.com/v1/wall?appid=16142&playerid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " >Your browser doesn't support iframes</iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Ayetstudio":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://www.ayetstudios.com/offers/web_offerwall/11096?external_identifier=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Notik":
			document.getElementById("iframe").innerHTML = `<iframe src='https://notik.me/coins?api_key=VUZeagwx7nqf8u4K1YaX0o95TkkVYoe7&pub_id=gnqI&user_id=${userid}'
		               style="width: 100%; height: 100%; border: none ;border-radius: 10px ";></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Cpalead":
			document.getElementById("iframe").innerHTML = `<iframe src="https://fastsvr.com/list/491571&subid=${userid} " style="width: 100%; height: 100%; border: none ;border-radius: 10px "; ></iframe>`;
			document.body.style.overflow = "hidden";
			break;

		case "Admantum":
			document.getElementById("iframe").innerHTML = ` <iframe src="https://www.admantum.com/offers?appid=23264&uid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Admantium":
			document.getElementById("iframe").innerHTML = ` <iframe  src="https://offerwall.admantium.net?offerwall=a6a58aa0-2f63-11ed-8d37-03516a247812&user_id=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Timewall":
			document.getElementById("iframe").innerHTML = `<iframe src="https://timewall.io/users/login?oid=4e703e9d6826477a&uid=${userid}"   style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "CpxResearch":
			document.getElementById("iframe").innerHTML = `<iframe src="https://offers.cpx-research.com/index.php?app_id=17106&ext_user_id=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px " ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Bitlabs":
			document.getElementById("iframe").innerHTML = `<iframe src="https://web.bitlabs.ai/?token=18537c9a-4a49-4a4f-88e6-371f44af9310&uid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe>`;
			document.body.style.overflow = "hidden";
			break;
		case "Wannads":
			document.getElementById("iframe").innerHTML = `<iframe src="https://wall.wannads.com/wall?apiKey=63a9bbb7e8d20454825288&userId=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Revenue":
			document.getElementById("iframe").innerHTML = `<iframe src="https://publishers.revenueuniverse.com/wallresp/508/offers?uid=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
		case "Mmwall":
			document.getElementById("iframe").innerHTML = `<iframe src="https://wall.make-money.top/?p=195&u=${userid}" style="width: 100%; height: 100%; border: none;border-radius: 10px "  ></iframe> `;
			document.body.style.overflow = "hidden";
			break;
	}

	// When the user clicks on the button, open the modal
	modal.style.display = "block";

	// When the user clicks on <span> (x), close the modal
	close.onclick = function() {
		modal.style.display = "none";
		document.body.style.overflow = "visible";

	};

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {

		if (event.target == modal) {
			modal.style.display = "none";
			document.body.style.overflow = "visible";
		}
	}
}
