(function(){"use strict";var e={4626:function(e,t,n){var r=n(9242),i=n(3396);const o={class:"container"},u=(0,i._)("h1",{align:"center"},"View files",-1);function s(e,t,n,r,s,a){const c=(0,i.up)("S3FileViewer");return(0,i.wg)(),(0,i.iD)("div",o,[u,(0,i.Wm)(c)])}var a=n(7139);const c={class:"request_input"},l=["href"];function f(e,t,n,o,u,s){return(0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i._)("div",{id:"drag-form",onDragover:t[1]||(t[1]=(0,r.iM)((()=>{}),["prevent"])),onDrop:t[2]||(t[2]=(0,r.iM)((()=>{}),["prevent"]))},[(0,i._)("div",c,[(0,i.wy)((0,i._)("input",{class:"request_input_field",type:"text",id:"drag-form-request-id","onUpdate:modelValue":t[0]||(t[0]=t=>e.request_id=t),placeholder:"Request ID",readonly:""},null,512),[[r.nr,e.request_id]])])],32),((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(e.items,((t,n)=>((0,i.wg)(),(0,i.iD)("li",{key:n},[(0,i._)("a",{style:{"text-decoration":"none"},href:`http://127.0.0.1:8000/object/get?request_id=${e.request_id}&filename=${t}`},(0,a.zw)(t),9,l)])))),128))],64)}var d=n(6265),p=n.n(d),h={name:"S3FileView",data:()=>({request_id:new URL(window.location.href).searchParams.get("request_id"),items:[]}),mounted(){this.getFiles()},methods:{getFiles:function(){p().get("http://127.0.0.1:8000/objects/list?request_id="+this.request_id).then((e=>{this.items=e.data,console.log(e)})).catch((e=>{this.$toast.show("Failed while trying to get files list: "+e.request.response,{type:"error",dismissible:!0,duration:!1}),console.log(e)}))}}},v=n(89);const g=(0,v.Z)(h,[["render",f],["__scopeId","data-v-1bcd7842"]]);var w=g,_={name:"App",components:{S3FileViewer:w}};const m=(0,v.Z)(_,[["render",s]]);var b=m,y=n(5860);(0,r.ri)(b).use(y.ZP).mount("#app")}},t={};function n(r){var i=t[r];if(void 0!==i)return i.exports;var o=t[r]={exports:{}};return e[r](o,o.exports,n),o.exports}n.m=e,function(){var e=[];n.O=function(t,r,i,o){if(!r){var u=1/0;for(l=0;l<e.length;l++){r=e[l][0],i=e[l][1],o=e[l][2];for(var s=!0,a=0;a<r.length;a++)(!1&o||u>=o)&&Object.keys(n.O).every((function(e){return n.O[e](r[a])}))?r.splice(a--,1):(s=!1,o<u&&(u=o));if(s){e.splice(l--,1);var c=i();void 0!==c&&(t=c)}}return t}o=o||0;for(var l=e.length;l>0&&e[l-1][2]>o;l--)e[l]=e[l-1];e[l]=[r,i,o]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={428:0};n.O.j=function(t){return 0===e[t]};var t=function(t,r){var i,o,u=r[0],s=r[1],a=r[2],c=0;if(u.some((function(t){return 0!==e[t]}))){for(i in s)n.o(s,i)&&(n.m[i]=s[i]);if(a)var l=a(n)}for(t&&t(r);c<u.length;c++)o=u[c],n.o(e,o)&&e[o]&&e[o][0](),e[o]=0;return n.O(l)},r=self["webpackChunkupload_logs"]=self["webpackChunkupload_logs"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=n.O(void 0,[998],(function(){return n(4626)}));r=n.O(r)})();
//# sourceMappingURL=viewer.b915df02.js.map