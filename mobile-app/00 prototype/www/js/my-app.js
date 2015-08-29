var myApp = new Framework7();   // Initialize your app
var $$ = Dom7;                  // Export selectors engine

// Add view
var mainView = myApp.addView('.view-main', {
    // Because we use fixed-through navbar we can enable dynamic navbar
    dynamicNavbar: true
});


$$(document).on('pageInit', function(e) {
    var page = e.detail.page;


    // TODO implement as a callback
    if (page.name === 'amount') {
        loadAmtPage();
        cache.category = page.query.cat;
    }

    if (page.name === 'summary') {
        loadSummaryPage();
    }
});



// class for data
var cache = {
    amount: 0.0,
    category: "other",
    lon: 0.0,
    lat: 0.0,
    country:"unknown",
    city:"unknown"
};



geolocate()
// GEOLOCATION
function geolocate() {

    geocoder = new google.maps.Geocoder();

    var onSuccess = function(pos) {
        var lat = parseFloat(pos.coords.latitude);
        var lng = parseFloat(pos.coords.longitude);
        var ll = new google.maps.LatLng(lat, lng);

        geocoder.geocode({'latLng': ll}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                if (results[0]){
                    var addressArray = results[0].address_components;
                    $$.each(addressArray, function(i, comp) {
                        if (comp.types[0] == "locality") {
                            cache.city = comp.long_name
                            return false;
                        } else if (comp.types[0] == "country") {
                            cache.country = comp.long_name
                            return false;
                        }
                    });

                } else {
                    alert("No results found :-(");
                }
            } else {
                alert("Google Geocoder issue: " + status);
            }
        });
    };

    var onError = function(err) {
        alert('error: ' + error.code + '\nmessage: ' + error.message);
    };

    navigator.geolocation.getCurrentPosition(onSuccess, onError)
};



// numpad functions
// TODO implement as class
function loadAmtPage() {
    $$('#numpad-1').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-2').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-3').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-4').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-5').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-6').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-7').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-8').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-9').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-0').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-dec').on('click', function(event) {addToNumfield($$(this).text())});
    $$('#numpad-clr').on('click', function(event) {$$('.numfield-txt').text("")});

    $$('#confirm').on('click', function(e) {
        cache.amount = parseFloat($$('.numfield-txt').html());
    });
};

function addToNumfield(val) {
    $$('.numfield-txt').append(val);
};


// SUMMARY PAGE classes

function loadSummaryPage() {
    $$("#category-selector").val(cache.category)
    $$("#expense-amount").val(cache.amount)
    $$("#location").val(cache.city + ", " + cache.country)

    $$('.form-to-json').on('click', function(event) {ajaxConnect()})
};


function ajaxConnect() {
//    var fd = myApp.formToJSON('#summary-form');
//    alert(JSON.stringify(fd));

    var fd = '{"date":"2015-05-14","category":"food & beverage","user":"philip","reimburseable":"True","amount":12.5}'
    console.log('hi')

    // var params = {
    //     method : 'POST',
    //     crossDomain : 'true',
    //     url : 'http://84.196.104.198:8080/expenses/',
    //     success : function(data, status, xhr) { alert (data); },
    //     error : function(xhr, status) {alert(xhr); alert(status);}
    // };

    $$.post('http://84.196.104.198:8080/expenses/', fd, function(data, status, xhr) {
       console.log('success')
    });
};
