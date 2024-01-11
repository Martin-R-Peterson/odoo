

// odoo.define('test_mindbite.tree_button', ['web.ListView', 'web.rpc'], function () {
//     "use strict";

//     var ListView = require('web.ListView');
//     var rpc = require('web.rpc');

//     var ListViewButton = ListView.include({
//         renderButtons: function ($node) {
//             var self = this;
//             this._super.apply(this, arguments);

//             if (this.$buttons) {
//                 var button = $('<button>', {
//                     class: 'btn btn-primary oe_highlight',
//                     text: _t('Fetch Data from API'),
//                 }).click(function () {
//                     rpc.query({
//                         model: 'test_mindbite',
//                         method: 'fetch_data_from_api',
//                     }).then(function () {
//                         self.reload();
//                     });
//                 });

//                 this.$buttons.find('.o_list_buttons').prepend(button);
//                 console.log("Button Loaded");
//             }
//         },
//     });

//     return ListViewButton;
// });