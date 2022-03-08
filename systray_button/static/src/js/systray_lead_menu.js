odoo.define('systray_button.address_systray', function (require) {
   "use strict";
   var core = require('web.core');
   var QWeb = core.qweb;
   var Widget = require('web.Widget');
   var SystrayMenu = require('web.SystrayMenu');
   var rpc = require('web.rpc');
   var Address = Widget.extend({
       template: 'systray_button.address_systray',
       xmlDependencies: ['/systray_button/static/src/js/systray_lead_menu.js'],
       events: {
           "click #add": "add_button"
       },
       add_button: function (event) {
           event.stopPropagation();
           var self = this;
           rpc.query({
               model: 'res.users',
               method: 'get_user_address',
               args: [],
           })
           .then(function (result){
               if (result){
                   self.$('#address').val(result);
               }
           });
       },

   });
   SystrayMenu.Items.push(Address);
   return Address;
});