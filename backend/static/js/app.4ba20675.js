(function(){"use strict";var e={3556:function(e,r,n){var t=n(9242),i=n(3396);const o={class:"container"},l=(0,i._)("h1",{align:"center"},"Upload logs",-1);function a(e,r,n,t,a,d){const u=(0,i.up)("DragAndDropForm");return(0,i.wg)(),(0,i.iD)("div",o,[l,(0,i.Wm)(u)])}var d=n(7139);const u=e=>((0,i.dD)("data-v-0d48091d"),e=e(),(0,i.Cn)(),e),s={class:"request_input"},c=(0,i.Uk)(" Drag & drop to upload "),f=u((()=>(0,i._)("div",null,"or browse",-1))),p={key:0},g=["index"],v=["onClick"];function h(e,r,n,o,l,a){return(0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i._)("div",{id:"drag-form",onDragover:r[5]||(r[5]=(0,t.iM)((()=>{}),["prevent"])),onDrop:r[6]||(r[6]=(0,t.iM)((()=>{}),["prevent"]))},[(0,i._)("div",s,[(0,i.wy)((0,i._)("input",{class:"request_input_field",type:"text",id:"drag-form-request-id","onUpdate:modelValue":r[0]||(r[0]=r=>e.request_id=r),placeholder:"Request ID"},null,512),[[t.nr,e.request_id]])]),(0,i._)("input",{id:"drag-form-input",style:{display:"none"},type:"file",multiple:"",onChange:r[1]||(r[1]=(...e)=>a.uploadFile&&a.uploadFile(...e))},null,32),(0,i._)("div",{onDrop:r[2]||(r[2]=(...e)=>a.dragFile&&a.dragFile(...e)),onDragover:r[3]||(r[3]=(0,t.iM)(((...e)=>a.dragover&&a.dragover(...e)),["prevent"])),onDragleave:r[4]||(r[4]=(0,t.iM)(((...e)=>a.dragleave&&a.dragleave(...e)),["prevent"])),id:"drag-field"},[c,f,e.File.length?((0,i.wg)(),(0,i.iD)("div",p,[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(e.File,((e,r)=>((0,i.wg)(),(0,i.iD)("ul",{key:e,index:r},[(0,i._)("li",null,[(0,i.Uk)((0,d.zw)(e.name)+" ",1),(0,i._)("button",{onClick:()=>a.deleteHandler(r),class:"google-button-cross"},"X",8,v)])],8,g)))),128))])):(0,i.kq)("",!0)],32)],32),(0,i._)("button",{class:"google-button",onClick:r[7]||(r[7]=(...e)=>a.clickHandler&&a.clickHandler(...e))},"Send")],64)}var _=n(6265),m=n.n(_),F={name:"DragAndDropForm",data:()=>({File:[],request_id:String()}),methods:{uploadFile(e){this.File=e.target.files},dragFile(e){this.File=e.dataTransfer.files,e.currentTarget.classList.remove("drag-field-file-hover")},dragover(e){e.currentTarget.classList.add("drag-field-file-hover")},dragleave(e){e.currentTarget.classList.remove("drag-field-file-hover")},clickHandler:function(e){console.log(e);let r=new FormData;r.append("request_id",this.request_id);for(let n=0;n<this.File.length;n++)m().post("http://127.0.0.1:8000/upload",{request_id:this.request_id,file:this.File[n]},{headers:{"Content-Type":"multipart/form-data"}}).then((e=>{console.log(e)}));this.request_id="",this.File=[]},deleteHandler:function(e){this.File=[...this.File].filter(((r,n)=>n!=e))}}},D=n(89);const b=(0,D.Z)(F,[["render",h],["__scopeId","data-v-0d48091d"]]);var w=b,k={name:"App",components:{DragAndDropForm:w}};const y=(0,D.Z)(k,[["render",a]]);var q=y;(0,t.ri)(q).mount("#app")}},r={};function n(t){var i=r[t];if(void 0!==i)return i.exports;var o=r[t]={exports:{}};return e[t](o,o.exports,n),o.exports}n.m=e,function(){var e=[];n.O=function(r,t,i,o){if(!t){var l=1/0;for(s=0;s<e.length;s++){t=e[s][0],i=e[s][1],o=e[s][2];for(var a=!0,d=0;d<t.length;d++)(!1&o||l>=o)&&Object.keys(n.O).every((function(e){return n.O[e](t[d])}))?t.splice(d--,1):(a=!1,o<l&&(l=o));if(a){e.splice(s--,1);var u=i();void 0!==u&&(r=u)}}return r}o=o||0;for(var s=e.length;s>0&&e[s-1][2]>o;s--)e[s]=e[s-1];e[s]=[t,i,o]}}(),function(){n.n=function(e){var r=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(r,{a:r}),r}}(),function(){n.d=function(e,r){for(var t in r)n.o(r,t)&&!n.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)}}(),function(){var e={143:0};n.O.j=function(r){return 0===e[r]};var r=function(r,t){var i,o,l=t[0],a=t[1],d=t[2],u=0;if(l.some((function(r){return 0!==e[r]}))){for(i in a)n.o(a,i)&&(n.m[i]=a[i]);if(d)var s=d(n)}for(r&&r(t);u<l.length;u++)o=l[u],n.o(e,o)&&e[o]&&e[o][0](),e[o]=0;return n.O(s)},t=self["webpackChunkfile_upload_service"]=self["webpackChunkfile_upload_service"]||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))}();var t=n.O(void 0,[998],(function(){return n(3556)}));t=n.O(t)})();
//# sourceMappingURL=app.4ba20675.js.map