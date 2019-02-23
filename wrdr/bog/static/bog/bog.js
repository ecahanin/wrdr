function write_to_box(word) {
	var listbox = document.getElementsByClassName("word-history")[0];
	var str = "<option";
	if (used.indexOf(word) == -1) {
		//if (valid_words.indexOf(word) == -1){
		//	str += ' class-"bad">' + word;
		//} else {
			if (!active) {
				str += ' class="missed">' + word;
			} else {
				str += ">" + word;
			}
		//}
		str += "</option>";
		listbox.innerHTML = str + listbox.innerHTML;
	}
}


function word_check() {
	var word = document.getElementById("entry").value.toUpperCase();
	if (valid_words.indexOf(word) > -1){
		if (used.indexOf(word) > -1){
			repeated_word(word);
		} else {
			write_to_box(word);
			used.push(word);
			update_remaining();
		}
	} else {
		bad_word(word);
	}
	document.getElementById("entry").value = "";
}

function bad_word() {
	/*flash box with red*/
}

function repeated_word() {
	/* do something with word */
}

function update_remaining() {
	remaining -= 1;
	var ticker = document.getElementById("remaining-ticker");
	if (remaining == 1) {
		ticker.textContent = "1 word remaining";
	} else {
		ticker.textContent = remaining + " words remaining";
	}
	if (remaining === 0) {
		end_round();
	}
}

var valid_words= [];
var remaining = 0
var used = [];
var active = true;

function get_valid_words(){
	var word_list = document.getElementsByClassName('valid');
	for (var i=0; i < word_list.length; i+=1){
		valid_words.push(word_list[i].textContent);
	}
	remaining = valid_words.length + 1;
	update_remaining();
}

function start_round() {
	used=[];
	get_valid_words();
	startTimer(30);
}

function startTimer(duration) {
    var start = Date.now();
    var diff;
    var minutes;
    var seconds;
    var display = document.getElementById("timer");
    function timer() {
        diff = duration - (((Date.now() - start) / 1000) | 0);
        minutes = (diff / 60) | 0;
        seconds = (diff % 60) | 0;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = minutes + ":" + seconds;
        if (diff <= 0) {
            start = Date.now() + 1000;
        }
        if (minutes == 0 && seconds == 0) {
            clearInterval(intervalId);
            end_round();
        }
    };
    
    timer();
    var intervalId = setInterval(timer, 1000);
}

function end_round() {
    active = false;
    var missed = [];
    for (i = 0; i < valid_words.length; i++){
        if (used.indexOf(valid_words[i]) == -1) {
            missed.push(valid_words[i]);
            write_to_box(valid_words[i]);
        }
    }
    
}