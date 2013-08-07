ckan.module('autocomplete-territory', function (jQuery, _) {
    return {
        initialize: function () {
            console.log('Ive been called for element: %o', this.el);
            $('.autocomplete-territories input').select2({
                ajax: {
                    data: function (term, page) {
                        return {
                            kind: ['ArrondissementOfCommuneOfFrance', 'CommuneOfFrance', 'DepartmentOfFrance',
                                'OverseasCollectivityOfFrance', 'RegionOfFrance'],
                            page: page,
                            term: term || ''
                        };
                    },
                    dataType: 'jsonp',
                    results: function (data, page) {
                        var results = [];
                        $.each(data.data.items, function (index, item) {
                            results.push({
                                id: item.kind + '/' + item.code,
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
                initSelection: function (element, callback) {
                    var count = 0;
                    var selectionData = [];
                    $(element.val().split(',')).each(function (index, kindCode) {
                        var splitKindCode = kindCode.split('/');
                        count += 1;
                        $.ajax('http://ou.comarquage.fr/api/v1/territory?jsonp=?', {
                            data: {
                                kind: splitKindCode[0],
                                code: splitKindCode[1]
                            },
                            dataType: 'json'
                        }).done(function (data) {
                            var item = data.data;
                            selectionData.push({
                                id: item.kind + '/' + item.code,
                                text: item.main_postal_distribution
                            });
                            if (selectionData.length >= count) {
                                callback(selectionData);
                            }
                        });
                    });
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
                            kind: ['ArrondissementOfCommuneOfFrance', 'CommuneOfFrance', 'DepartmentOfFrance',
                                'OverseasCollectivityOfFrance', 'RegionOfFrance'],
                            page: page,
                            term: term || ''
                        };
                    },
                    dataType: 'jsonp',
                    results: function (data, page) {
                        var results = [];
                        $.each(data.data.items, function (index, item) {
                            results.push({
                                id: item.kind + '/' + item.code,
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
                initSelection: function (element, callback) {
                    var kindCode = $(element).val();
                    if (kindCode !== '') {
                        var splitKindCode = kindCode.split('/');
                        $.ajax('http://ou.comarquage.fr/api/v1/territory?jsonp=?', {
                            data: {
                                kind: splitKindCode[0],
                                code: splitKindCode[1]
                            },
                            dataType: 'json'
                        }).done(function (data) {
                            var item = data.data;
                            callback({
                                id: item.kind + '/' + item.code,
                                text: item.main_postal_distribution
                            });
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
