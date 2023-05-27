(function ($) {
  // Function to fetch provinces based on the selected country
  function fetchProvinces() {
    var countryId = $('#id_country').val();

    // Make an AJAX request to fetch provinces
    $.ajax({
      url: '/address/provinces/',
      data: {
        country_id: countryId
      },
      success: function (data) {
        // Clear the existing province options
        $('#id_province').empty();

        // Append the fetched province options
        $.each(data.provinces, function (index, province) {
          $('#id_province').append(
            $('<option></option>').val(province.id).text(province.name)
          );
        });
      }
    });
  }

  // Function to fetch municipalities based on the selected province
  function fetchMunicipalities() {
    var provinceId = $('#id_province').val();

    // Make an AJAX request to fetch municipalities
    $.ajax({
      url: '/address/municipalities/', 
      data: {
        province_id: provinceId
      },
      success: function (data) {
        // Clear the existing municipality options
        $('#id_municipality').empty();

        // Append the fetched municipality options
        $.each(data.municipalities, function (index, municipality) {
          $('#id_municipality').append(
            $('<option></option>').val(municipality.id).text(municipality.name)
          );
        });
      }
    });
  }

  // Event handler for the country selection change
  $(document).on('change', '#id_country', function () {
    fetchProvinces();
  });

  // Event handler for the province selection change
  $(document).on('change', '#id_province', function () {
    fetchMunicipalities();
  });

})(jQuery);
