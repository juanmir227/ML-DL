function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var model = document.getElementById("uiModels");
    var year = document.getElementById('uiYear');
    var fuel = document.getElementById('uiFuels');
    var km_driven = document.getElementById('uiKm');
    var seller = document.getElementById('uiSeller');
    var transmission = document.getElementById('uiTransmission');
    var owner = document.getElementById('uiOwner');
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_car_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

    $.post(url, {
        car_model: model.value,
        year: parseInt(year.value),
        km_driven: parseInt(km_driven.value),
        fuel: fuel.value,
        seller: seller.value,
        transmission: transmission.value,
        owner: owner.value,
    }, function (data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " USD</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");

    var url = "http://127.0.0.1:5000/get_car_models"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_car_models"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url, function (data, status) {
        console.log("got response for get_car_models request");
        if (data) {
            var car_models = data.car_models;
            var uiModels = document.getElementById("uiModels");
            $('#uiModels').empty();
            for (var i in car_models) {
                var opt = new Option(car_models[i]);
                $('#uiModels').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;