ckan.module('autocomplete-territory', function (jQuery, _) {
    return {
        initialize: function () {
            $('.autocomplete-territories input').select2({
                ajax: {
                    data: function (term, page) {
                        return {
                            kind: ['ArrondissementOfCommuneOfFrance', 'CommuneOfFrance', 'Country',
                                'DepartmentOfFrance', 'InternationalOrganization', 'OverseasCollectivityOfFrance',
                                'RegionOfFrance'],
                            page: page,
                            term: term || ''
                        };
                    },
                    dataType: 'jsonp',
                    results: function (data, page) {
                        var results = [];
                        $.each(data.data.items, function (index, item) {
                            results.push({
                                id: item.kind + '/' + item.code + '/' + item.main_postal_distribution,
                                text: item.main_postal_distribution
                            });
                        });
                        return {
                            results: results,
                            more: data.data.pageIndex < data.data.totalPages
                        };
                    },
                    // Add traditional flag. It is not supported by select2 ajax, so we add it using transport option.
                    transport: function(options) {
                        return $.ajax($.extend({}, options, {
                            traditional: true
                        }));
                    },
                    url: 'http://ou.comarquage.fr/api/v1/autocomplete-territory?jsonp=?'
                },
                allowClear: true,
                initSelection: function (element, callback) {
                    var count = 0;
                    var selectionData = [];
                    $(element.val().split(',')).each(function (index, kindCodeName) {
                        var splitKindCodeName = kindCodeName.split('/');
                        selectionData.push({
                            id: kindCodeName,
                            text: splitKindCodeName[2]
                        });
                    });
                    callback(selectionData);
                },
                multiple: true,
                placeholder: this.el.attr('placeholder') || 'Où...',
//                width: 'resolve'
                width: '100%'
            });

            $('.autocomplete-territory').select2({
                ajax: {
                    data: function (term, page) {
                        return {
                            kind: ['ArrondissementOfCommuneOfFrance', 'CommuneOfFrance', 'Country',
                                'DepartmentOfFrance', 'InternationalOrganization', 'OverseasCollectivityOfFrance',
                                'RegionOfFrance'],
                            page: page,
                            term: term || ''
                        };
                    },
                    dataType: 'jsonp',
                    results: function (data, page) {
                        var results = [];
                        $.each(data.data.items, function (index, item) {
                            results.push({
                                id: item.kind + '/' + item.code + '/' + item.main_postal_distribution,
                                text: item.main_postal_distribution
                            });
                        });
                        return {
                            results: results,
                            more: data.data.pageIndex < data.data.totalPages
                        };
                    },
                    // Add traditional flag. It is not supported by select2 ajax, so we add it using transport option.
                    transport: function(options) {
                        return $.ajax($.extend({}, options, {
                            traditional: true
                        }));
                    },
                    url: 'http://ou.comarquage.fr/api/v1/autocomplete-territory?jsonp=?'
                },
                allowClear: true,
                initSelection: function (element, callback) {
                    var kindCodeName = $(element).val();
                    if (kindCodeName !== '') {
                        var splitKindCodeName = kindCodeName.split('/');
                        callback({
                            id: kindCodeName,
                            text: splitKindCodeName[2]
                        });
                    }
                },
                placeholder: this.el.attr('placeholder') || 'Où...',
//                width: 'resolve'
                width: '100%'
            });
        }
    };
});
