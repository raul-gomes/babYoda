function inicializar() {
    var coordenadas = {lat: -15.80762866191734, lng: -48.09639308638717};

    var mapa = new google.maps.Map(document.getElementById('mapa'), {
      zoom: 18,
      center: coordenadas,
      zoomControl: false,
      mapTypeControl: false,

    });

    var marker = new google.maps.Marker({
      position: coordenadas,
      map: mapa,
      title: "babYoda chá"
    });
  }