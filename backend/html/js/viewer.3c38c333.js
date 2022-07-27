(function(){"use strict";var e={8612:function(e,t,r){var i=r(9242),n=r(3396);const s={class:"container"},o=(0,n._)("h1",{align:"center"},"View files",-1);function u(e,t,r,i,u,a){const c=(0,n.up)("S3FileViewer");return(0,n.wg)(),(0,n.iD)("div",s,[o,(0,n.Wm)(c)])}var a=r(7139);const c=e=>((0,n.dD)("data-v-3c294720"),e=e(),(0,n.Cn)(),e),l={class:"request_input"},d={style:{width:"60%"}},f=c((()=>(0,n._)("th",{style:{width:"25%"}},"Created at",-1))),h=["href"],p={class:"td-center"},m={class:"td-center"};function w(e,t,r,s,o,u){return(0,n.wg)(),(0,n.iD)(n.HY,null,[(0,n._)("div",{id:"drag-form",onDragover:t[2]||(t[2]=(0,i.iM)((()=>{}),["prevent"])),onDrop:t[3]||(t[3]=(0,i.iM)((()=>{}),["prevent"]))},[(0,n._)("div",l,[(0,n.wy)((0,n._)("input",{class:"request_input_field",type:"text",id:"drag-form-request-id","onUpdate:modelValue":t[0]||(t[0]=t=>e.request_id=t),placeholder:"Request ID",onKeyup:t[1]||(t[1]=(0,i.D2)(((...e)=>u.searchRequest&&u.searchRequest(...e)),["enter"]))},null,544),[[i.nr,e.request_id]])])],32),(0,n._)("table",d,[(0,n._)("tr",null,[(0,n._)("th",{style:{cursor:"pointer"},onClick:t[4]||(t[4]=(...e)=>u.sortByName&&u.sortByName(...e))},"Filename"),(0,n._)("th",{style:{width:"25%",cursor:"pointer"},onClick:t[5]||(t[5]=(...e)=>u.sortBySize&&u.sortBySize(...e))},"Size"),f]),((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(e.items,((e,t)=>((0,n.wg)(),(0,n.iD)("tr",{key:t},[(0,n._)("td",null,[(0,n._)("a",{style:{"text-decoration":"none"},href:`https://files.mobius-it.ru/object/get?filename=${e.name}`},(0,a.zw)(e.name),9,h)]),(0,n._)("td",p,(0,a.zw)(e.size),1),(0,n._)("td",m,(0,a.zw)(e.created),1)])))),128))])],64)}var v=r(6265),_=r.n(v),g={name:"S3FileView",data:()=>({request_id:new URL(window.location.href).searchParams.get("request_id"),items:[],nameSortOrder:!0,sizeSortOrder:!0,dateSortOrder:!0}),mounted(){this.getFiles()},methods:{getFiles:function(){_().get("https://files.mobius-it.ru/object/list?request_id="+this.request_id).then((e=>{this.items=e.data,console.log(e)})).catch((e=>{this.$toast.show("Failed while trying to get files list. "+e.request.response,{type:"error",dismissible:!0,duration:!1}),console.log(e)}))},searchRequest:function(){window.location.href="https://files.mobius-it.ru/view?request_id="+this.request_id},sortByName:function(){this.nameSortOrder?(this.nameSortOrder=!1,this.items=this.items.slice().sort((function(e,t){return e.name>t.name?1:-1}))):(this.nameSortOrder=!0,this.items=this.items.slice().sort((function(e,t){return e.name<t.name?1:-1})))},sortBySize:function(){this.sizeSortOrder?(this.sizeSortOrder=!1,this.items=this.items.slice().sort((function(e,t){return parseFloat(e.size)>parseFloat(t.size)?1:-1}))):(this.sizeSortOrder=!0,this.items=this.items.slice().sort((function(e,t){return parseFloat(e.size)<parseFloat(t.size)?1:-1})))},startDownloading:function(e){this.$toast.show(`Download of ${e} started`,{type:"success",dismissible:!0,duration:4e3})}}},y=r(89);const b=(0,y.Z)(g,[["render",w],["__scopeId","data-v-3c294720"]]);var O=b,q={name:"App",components:{S3FileViewer:O}};const z=(0,y.Z)(q,[["render",u]]);var S=z,F=r(5860);(0,i.ri)(S).use(F.ZP).mount("#app")}},t={};function r(i){var n=t[i];if(void 0!==n)return n.exports;var s=t[i]={exports:{}};return e[i](s,s.exports,r),s.exports}r.m=e,function(){var e=[];r.O=function(t,i,n,s){if(!i){var o=1/0;for(l=0;l<e.length;l++){i=e[l][0],n=e[l][1],s=e[l][2];for(var u=!0,a=0;a<i.length;a++)(!1&s||o>=s)&&Object.keys(r.O).every((function(e){return r.O[e](i[a])}))?i.splice(a--,1):(u=!1,s<o&&(o=s));if(u){e.splice(l--,1);var c=n();void 0!==c&&(t=c)}}return t}s=s||0;for(var l=e.length;l>0&&e[l-1][2]>s;l--)e[l]=e[l-1];e[l]=[i,n,s]}}(),function(){r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,{a:t}),t}}(),function(){r.d=function(e,t){for(var i in t)r.o(t,i)&&!r.o(e,i)&&Object.defineProperty(e,i,{enumerable:!0,get:t[i]})}}(),function(){r.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={428:0};r.O.j=function(t){return 0===e[t]};var t=function(t,i){var n,s,o=i[0],u=i[1],a=i[2],c=0;if(o.some((function(t){return 0!==e[t]}))){for(n in u)r.o(u,n)&&(r.m[n]=u[n]);if(a)var l=a(r)}for(t&&t(i);c<o.length;c++)s=o[c],r.o(e,s)&&e[s]&&e[s][0](),e[s]=0;return r.O(l)},i=self["webpackChunkupload_logs"]=self["webpackChunkupload_logs"]||[];i.forEach(t.bind(null,0)),i.push=t.bind(null,i.push.bind(i))}();var i=r.O(void 0,[998],(function(){return r(8612)}));i=r.O(i)})();
//# sourceMappingURL=viewer.3c38c333.js.map