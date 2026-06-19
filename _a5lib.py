CSS = r'''
:root{--bg:#0a0e1a;--bg2:#0f1626;--panel:#121a2e;--panel2:#16203a;--line:#1f2b47;--line2:#27365a;--txt:#e6edf7;--mut:#8ea0c0;--mut2:#5f7194;--acc:#3ba2ff;--acc2:#1f6fd6;--grn:#2fd07f;--ylw:#f6c344;--red:#ff5c6c;--pur:#9b7bff;--cy:#33d6e0;--org:#ff9d42;--chip:#1a2540;--r:10px;--sh:0 8px 28px rgba(0,0,0,.45)}
*{box-sizing:border-box;margin:0;padding:0}html,body{height:100%}
body{font-family:'Segoe UI',Inter,system-ui,Arial,sans-serif;background:radial-gradient(1200px 600px at 85% -10%,rgba(59,162,255,.10),transparent),radial-gradient(900px 500px at 0% 110%,rgba(155,123,255,.08),transparent),var(--bg);color:var(--txt);font-size:13.5px;overflow:hidden}
.app{display:grid;grid-template-columns:252px 1fr;grid-template-rows:56px 1fr;height:100vh}
.top{grid-column:1/3;display:flex;align-items:center;gap:14px;padding:0 16px;background:linear-gradient(180deg,#101a30,#0c1322);border-bottom:1px solid var(--line);z-index:30}
.brand{display:flex;align-items:center;gap:10px;min-width:236px}.logo{width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--grn),var(--cy));display:grid;place-items:center;font-weight:800;color:#06101f;box-shadow:0 0 16px rgba(47,208,127,.5);font-size:12px}
.brand b{font-size:13px}.brand small{display:block;color:var(--mut2);font-size:9.5px;font-weight:700;letter-spacing:.3px}
.search{flex:1;max-width:480px;display:flex;align-items:center;gap:8px;background:#0c1426;border:1px solid var(--line);border-radius:8px;padding:7px 12px;color:var(--mut)}
.search input{flex:1;background:none;border:none;color:var(--txt);outline:none;font-size:12.5px}
.tbtns{display:flex;gap:6px;flex-wrap:wrap}.tb{background:var(--chip);border:1px solid var(--line2);color:var(--txt);padding:7px 11px;border-radius:7px;font-size:11.5px;cursor:pointer;white-space:nowrap;transition:.15s;font-weight:600}
.tb:hover{border-color:var(--acc);color:var(--acc);box-shadow:0 0 0 2px rgba(59,162,255,.12)}.tb.pri{background:linear-gradient(135deg,var(--grn),#1f9d63);border:none;color:#04140c}.tb.dng{border-color:rgba(255,92,108,.4);color:var(--red)}
.top .right{display:flex;align-items:center;gap:12px;margin-left:auto}.bell{position:relative;cursor:pointer;color:var(--mut)}
.bell b{position:absolute;top:-6px;right:-8px;background:var(--red);color:#fff;font-size:9px;border-radius:10px;padding:1px 5px;font-weight:700}
.me{display:flex;align-items:center;gap:8px}.av{width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,var(--grn),var(--cy));display:grid;place-items:center;font-weight:700;color:#06101f}
.side{background:linear-gradient(180deg,#0d1424,#0a0f1c);border-right:1px solid var(--line);overflow-y:auto;padding:10px 8px}
.side::-webkit-scrollbar{width:7px}.side::-webkit-scrollbar-thumb{background:#22304f;border-radius:6px}
.snav{font-size:9.5px;text-transform:uppercase;letter-spacing:1.1px;color:var(--mut2);padding:12px 10px 5px;font-weight:800}
.mi{display:flex;align-items:center;gap:9px;padding:8px 10px;border-radius:7px;color:var(--mut);cursor:pointer;font-size:12px;font-weight:600;transition:.12s}
.mi:hover{background:#13203b;color:var(--txt)}.mi.on{background:linear-gradient(90deg,rgba(47,208,127,.18),transparent);color:#fff;box-shadow:inset 2px 0 0 var(--grn)}
.mi .ic{width:16px;text-align:center}.mi .badge{margin-left:auto;background:var(--chip);color:var(--mut);border-radius:10px;padding:1px 7px;font-size:10px;font-weight:700}
.mi .badge.r{background:rgba(255,92,108,.18);color:var(--red)}.mi .badge.y{background:rgba(246,195,68,.18);color:var(--ylw)}
.modlink{display:flex;align-items:center;gap:8px;padding:7px 10px;margin-top:4px;border-radius:7px;color:var(--mut2);font-size:11px;cursor:pointer}
.modlink:hover{background:#11203a;color:var(--cy)}.modlink b{margin-left:auto;font-size:9px;color:var(--mut2)}
.main{overflow-y:auto;padding:16px 18px 50px}.main::-webkit-scrollbar{width:9px}.main::-webkit-scrollbar-thumb{background:#22304f;border-radius:6px}
.crumbs{display:flex;align-items:center;gap:7px;color:var(--mut2);font-size:11px;margin-bottom:10px}.crumbs b{color:var(--txt)}
.hbar{display:flex;align-items:flex-start;gap:12px}.h1{font-size:18px;font-weight:800}.h1 small{display:block;color:var(--mut);font-size:11.5px;font-weight:500;margin-top:3px}
.modeswitch{display:inline-flex;background:var(--bg2);border:1px solid var(--line2);border-radius:9px;padding:3px;gap:3px;margin-left:auto}
.modeswitch .ms{padding:6px 13px;border-radius:7px;font-size:11.5px;color:var(--mut);cursor:pointer;font-weight:700}.modeswitch .ms.on{background:linear-gradient(135deg,var(--grn),#1f9d63);color:#04140c}
.tabs{display:flex;gap:4px;flex-wrap:wrap;margin:14px 0;border-bottom:1px solid var(--line)}
.tab{padding:8px 11px;border-radius:7px 7px 0 0;color:var(--mut);font-size:11.5px;cursor:pointer;font-weight:600;border:1px solid transparent;border-bottom:none}
.tab:hover{color:var(--txt);background:#101a30}.tab.on{color:#fff;background:var(--panel);border-color:var(--line);box-shadow:inset 0 2px 0 var(--grn)}
.view{display:none;animation:fade .25s}.view.on{display:block}@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1}}
.kgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:11px}
.kpi{background:linear-gradient(160deg,var(--panel),var(--bg2));border:1px solid var(--line);border-radius:var(--r);padding:13px 14px;position:relative;overflow:hidden}
.kpi:before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--acc)}
.kpi.g:before{background:var(--grn)}.kpi.y:before{background:var(--ylw)}.kpi.r:before{background:var(--red)}.kpi.p:before{background:var(--pur)}.kpi.c:before{background:var(--cy)}.kpi.o:before{background:var(--org)}
.kpi .lbl{color:var(--mut);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.4px}.kpi .val{font-size:23px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.kpi .sub{font-size:10.5px;color:var(--mut2);margin-top:3px}.up{color:var(--grn)}.dn{color:var(--red)}
.grid2{display:grid;grid-template-columns:1fr 366px;gap:14px;margin-top:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:14px}
@media(max-width:1300px){.grid2{grid-template-columns:1fr}.grid3{grid-template-columns:1fr 1fr}}
.card{background:linear-gradient(160deg,var(--panel),var(--bg2));border:1px solid var(--line);border-radius:var(--r);padding:14px}
.card h3{font-size:13px;font-weight:700;display:flex;align-items:center;gap:8px;margin-bottom:10px}.card h3 .t{margin-left:auto;font-size:10.5px;color:var(--mut2);font-weight:600}
.hint{color:var(--mut2);font-size:11px}
.donutwrap{display:flex;align-items:center;gap:16px}.donut{width:128px;height:128px;border-radius:50%;display:grid;place-items:center;flex-shrink:0}
.donut .inner{width:96px;height:96px;border-radius:50%;background:var(--panel);display:grid;place-items:center;text-align:center}.donut .inner b{font-size:26px;display:block}.donut .inner small{color:var(--mut);font-size:9.5px}
.dim{display:grid;grid-template-columns:120px 1fr 40px;gap:9px;align-items:center;padding:6px 0;border-bottom:1px dashed rgba(31,43,71,.6);font-size:11.5px}
.bar{height:7px;border-radius:6px;background:#1c2742;overflow:hidden;min-width:54px}.bar i{display:block;height:100%;border-radius:6px}
.map{position:relative;height:440px;border-radius:var(--r);overflow:hidden;border:1px solid var(--line2);background:radial-gradient(420px 280px at 30% 35%,rgba(47,208,127,.10),transparent),radial-gradient(380px 260px at 70% 65%,rgba(255,92,108,.10),transparent),linear-gradient(180deg,#0b1424,#0a1120)}
.grid-lines{position:absolute;inset:0;background-image:linear-gradient(rgba(120,150,200,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(120,150,200,.06) 1px,transparent 1px);background-size:42px 42px}
.ti{position:absolute;border:1.5px dashed rgba(47,208,127,.55);background:rgba(47,208,127,.06);border-radius:14px;font-size:9.5px;color:#bff0d4;padding:3px 6px;cursor:pointer;transition:.15s}.ti:hover{background:rgba(47,208,127,.16);box-shadow:0 0 0 2px rgba(47,208,127,.25)}.ti.bad{border-color:rgba(255,92,108,.6);background:rgba(255,92,108,.08);color:#ffc2c8}
.heat{position:absolute;border-radius:50%;transform:translate(-50%,-50%);pointer-events:none;filter:blur(7px)}
.dot{position:absolute;width:11px;height:11px;border-radius:50%;transform:translate(-50%,-50%);cursor:pointer;box-shadow:0 0 0 4px rgba(255,255,255,.06)}
.dot.err{background:var(--red);box-shadow:0 0 10px var(--red),0 0 0 4px rgba(255,92,108,.18)}.dot.warn{background:var(--ylw)}.dot.ok{background:var(--grn)}.dot.sens{background:var(--pur);box-shadow:0 0 10px var(--pur),0 0 0 4px rgba(155,123,255,.18)}.dot.dup{background:var(--org)}
.pulse{animation:pl 1.8s infinite}@keyframes pl{0%{box-shadow:0 0 0 0 rgba(255,92,108,.5)}70%{box-shadow:0 0 0 12px rgba(255,92,108,0)}100%{box-shadow:0 0 0 0 rgba(255,92,108,0)}}
.maptools{position:absolute;top:10px;left:10px;display:flex;flex-direction:column;gap:6px;z-index:5}.mt{width:30px;height:30px;background:rgba(12,20,38,.85);border:1px solid var(--line2);border-radius:7px;display:grid;place-items:center;cursor:pointer;color:var(--mut)}.mt:hover{color:var(--acc);border-color:var(--acc)}
.maplayers{position:absolute;top:10px;right:10px;background:rgba(8,14,26,.9);border:1px solid var(--line2);border-radius:8px;padding:9px 11px;font-size:10.5px;z-index:5;width:192px}
.maplayers .lt{font-weight:700;color:var(--mut);margin-bottom:5px;font-size:10px;text-transform:uppercase;letter-spacing:.4px}
.maplayers .ly{display:flex;align-items:center;gap:7px;padding:3px 0;cursor:pointer}.maplayers .ly i{width:9px;height:9px;border-radius:2px}
.maplayers .sw{margin-left:auto;width:26px;height:14px;border-radius:8px;background:var(--grn);position:relative}.maplayers .sw:after{content:"";position:absolute;right:2px;top:2px;width:10px;height:10px;border-radius:50%;background:#04140c}
.maplayers .sw.off{background:#33405e}.maplayers .sw.off:after{left:2px;right:auto;background:var(--mut)}
.legend{position:absolute;bottom:10px;left:10px;background:rgba(8,14,26,.88);border:1px solid var(--line2);border-radius:8px;padding:8px 10px;font-size:10.5px;display:flex;flex-direction:column;gap:5px;z-index:5}.legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px}
table{width:100%;border-collapse:collapse;font-size:12px}th{text-align:left;color:var(--mut2);font-size:10px;text-transform:uppercase;letter-spacing:.5px;padding:8px 9px;border-bottom:1px solid var(--line);font-weight:700;position:sticky;top:0;background:var(--panel)}
td{padding:9px;border-bottom:1px solid rgba(31,43,71,.55)}tr:hover td{background:rgba(47,208,127,.05);cursor:pointer}
.tw{max-height:410px;overflow:auto}.tw::-webkit-scrollbar{width:8px}.tw::-webkit-scrollbar-thumb{background:#22304f;border-radius:6px}
.pill{display:inline-flex;align-items:center;gap:5px;padding:2px 9px;border-radius:20px;font-size:10.5px;font-weight:700}.pill:before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
.p-ok{color:var(--grn);background:rgba(47,208,127,.12)}.p-warn{color:var(--ylw);background:rgba(246,195,68,.12)}.p-err{color:var(--red);background:rgba(255,92,108,.12)}.p-idle{color:var(--mut);background:rgba(95,113,148,.14)}.p-info{color:var(--acc);background:rgba(59,162,255,.12)}.p-pur{color:var(--pur);background:rgba(155,123,255,.12)}.p-org{color:var(--org);background:rgba(255,157,66,.12)}
.subtag{font-size:10px;padding:1px 7px;border-radius:5px;font-weight:700;white-space:nowrap}
.s-pub{background:rgba(47,208,127,.14);color:var(--grn)}.s-int{background:rgba(59,162,255,.14);color:var(--acc)}.s-rest{background:rgba(246,195,68,.14);color:var(--ylw)}.s-sens{background:rgba(255,157,66,.16);color:var(--org)}.s-asens{background:rgba(255,92,108,.16);color:var(--red)}.s-sig{background:rgba(155,123,255,.16);color:var(--pur)}
.rp{background:linear-gradient(160deg,var(--panel),var(--bg2));border:1px solid var(--line);border-radius:var(--r);padding:14px;align-self:start;position:sticky;top:4px}
.rp .hd{display:flex;align-items:center;gap:10px;padding-bottom:11px;border-bottom:1px solid var(--line);margin-bottom:11px}.rp .hd .ico{width:36px;height:36px;border-radius:9px;background:rgba(255,92,108,.16);display:grid;place-items:center;font-size:17px}
.rp .hd b{font-size:13px}.rp .hd small{color:var(--mut);font-size:10.5px;display:block}
.kv{display:flex;justify-content:space-between;gap:8px;padding:6px 0;border-bottom:1px dashed rgba(31,43,71,.6);font-size:11.5px}.kv span{color:var(--mut)}.kv b{font-weight:700;text-align:right}
.acts{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px}.acts .tb{flex:1;text-align:center;min-width:78px}
.ai{background:linear-gradient(135deg,rgba(155,123,255,.13),rgba(59,162,255,.06));border:1px solid rgba(155,123,255,.35);border-radius:10px;padding:12px;margin-top:11px}
.ai .ah{display:flex;align-items:center;gap:8px;font-weight:700;font-size:12px;color:#cdbcff;margin-bottom:7px}.ai .ah .dot2{width:8px;height:8px;border-radius:50%;background:var(--pur);box-shadow:0 0 10px var(--pur)}
.ai p{font-size:11.5px;color:#d7ddf0;line-height:1.55}.ai .rec{background:rgba(8,14,26,.4);border-left:2px solid var(--pur);padding:7px 9px;border-radius:6px;margin-top:7px;font-size:11px}
.agrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.agent{background:linear-gradient(160deg,var(--panel),var(--bg2));border:1px solid var(--line);border-radius:10px;padding:13px}
.agent .top2{display:flex;align-items:center;gap:10px;margin-bottom:8px}.agent .ab{width:38px;height:38px;border-radius:9px;background:linear-gradient(135deg,var(--pur),var(--acc));display:grid;place-items:center;font-size:18px}
.agent b{font-size:12.5px}.agent .st{margin-left:auto}.agent p{font-size:11px;color:var(--mut);line-height:1.5;margin:6px 0}
.agent .ex{background:rgba(155,123,255,.08);border:1px solid rgba(155,123,255,.2);border-radius:7px;padding:7px 9px;font-size:10.5px;color:#cdbcff;font-style:italic;margin-top:6px}.agent ul{margin:4px 0 0 16px;font-size:10.5px;color:var(--mut)}
.flow{display:flex;align-items:stretch;gap:0;overflow-x:auto;padding:10px 2px}
.fnode{min-width:112px;background:var(--panel2);border:1px solid var(--line2);border-radius:9px;padding:10px;text-align:center;font-size:11px;flex-shrink:0}.fnode .fi{font-size:18px}.fnode b{display:block;margin-top:4px;font-size:10.5px}.fnode small{color:var(--mut2);font-size:9px}
.farr{display:flex;align-items:center;color:var(--grn);font-size:17px;padding:0 5px;flex-shrink:0}
.fnode.gis{border-color:var(--grn);box-shadow:0 0 0 1px rgba(47,208,127,.3)}.fnode.ai{border-color:var(--pur);box-shadow:0 0 0 1px rgba(155,123,255,.3)}.fnode.aud{border-color:var(--cy)}
.kan{display:grid;grid-template-columns:repeat(auto-fill,minmax(182px,1fr));gap:10px}.kcol{background:var(--bg2);border:1px solid var(--line);border-radius:9px;padding:9px;min-height:120px}
.kcol h4{font-size:10px;color:var(--mut);display:flex;align-items:center;gap:6px;margin-bottom:8px;text-transform:uppercase;letter-spacing:.4px}.kcol h4 b{margin-left:auto;background:var(--chip);border-radius:10px;padding:0 7px;font-size:9.5px}
.kc{background:var(--panel2);border:1px solid var(--line2);border-radius:7px;padding:9px;margin-bottom:7px;cursor:pointer;font-size:11px;border-left:3px solid var(--acc)}.kc:hover{border-color:var(--acc)}
.kc.h{border-left-color:var(--red)}.kc.m{border-left-color:var(--ylw)}.kc.l{border-left-color:var(--grn)}
.kc .kt{font-weight:700;font-size:11px}.kc .km{color:var(--mut2);font-size:10px;margin-top:3px;display:flex;gap:6px;flex-wrap:wrap}
.steps{display:flex;gap:0;margin-bottom:16px;flex-wrap:wrap}.step{flex:1;min-width:88px;text-align:center;position:relative;padding:8px 4px;cursor:pointer}
.step .sn{width:26px;height:26px;border-radius:50%;background:var(--chip);border:1px solid var(--line2);display:grid;place-items:center;margin:0 auto 6px;font-weight:700;font-size:11px;color:var(--mut)}
.step.on .sn{background:linear-gradient(135deg,var(--grn),#1f9d63);color:#04140c;border:none}.step.done .sn{background:var(--acc);color:#04140c;border:none}.step small{font-size:10px;color:var(--mut)}.step.on small{color:#fff}
.step:after{content:"";position:absolute;top:21px;left:60%;right:-40%;height:2px;background:var(--line2)}.step:last-child:after{display:none}
.frm{display:grid;grid-template-columns:1fr 1fr;gap:11px}.fg{display:flex;flex-direction:column;gap:5px}.fg label{font-size:10.5px;color:var(--mut);font-weight:600}
.fg input,.fg select,.fg textarea{background:#0c1426;border:1px solid var(--line2);border-radius:7px;padding:8px 10px;color:var(--txt);font-size:12px;outline:none;font-family:inherit}.fg input:focus,.fg select:focus,.fg textarea:focus{border-color:var(--grn)}.full{grid-column:1/3}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.tag{background:var(--chip);border:1px solid var(--line2);border-radius:6px;padding:2px 8px;font-size:10px;color:var(--mut)}
.sel{outline:2px solid var(--grn)!important;outline-offset:-1px}
.lin{display:flex;align-items:center;gap:0;overflow-x:auto;padding:16px 4px}.lnode{min-width:114px;text-align:center;flex-shrink:0;background:var(--panel2);border:1px solid var(--line2);border-radius:9px;padding:11px 9px;font-size:11px}
.lnode .li{font-size:17px}.lnode b{display:block;font-size:10px;margin-top:4px}.lnode small{font-size:9px;color:var(--mut2)}.larr{color:var(--cy);padding:0 5px;font-size:16px;flex-shrink:0}
.lnode.src{border-color:var(--acc)}.lnode.gis{border-color:var(--grn)}.lnode.out{border-color:var(--pur)}
.matrix td,.matrix th{text-align:center}.matrix td:first-child,.matrix th:first-child{text-align:left}.chk{font-size:13px}.y{color:var(--grn)}.n{color:var(--red)}.pa{color:var(--ylw)}
.simbanner{background:linear-gradient(90deg,rgba(246,195,68,.18),transparent);border:1px solid rgba(246,195,68,.4);border-radius:8px;padding:9px 13px;font-size:11.5px;color:var(--ylw);margin-bottom:12px;display:flex;align-items:center;gap:8px;font-weight:600}
.spark{display:flex;align-items:flex-end;gap:3px;height:46px}.spark i{flex:1;background:linear-gradient(180deg,var(--grn),rgba(47,208,127,.15));border-radius:2px 2px 0 0;min-width:5px}
.barchart{display:flex;flex-direction:column;gap:8px}.barrow{display:grid;grid-template-columns:150px 1fr 44px;gap:9px;align-items:center;font-size:11px}
.timeline{position:relative;padding-left:18px}.timeline:before{content:"";position:absolute;left:5px;top:4px;bottom:4px;width:2px;background:var(--line2)}
.tl{position:relative;padding:7px 0 7px 4px;font-size:11.5px}.tl:before{content:"";position:absolute;left:-16px;top:11px;width:9px;height:9px;border-radius:50%;background:var(--acc);box-shadow:0 0 0 3px var(--bg)}
.tl.ok:before{background:var(--grn)}.tl.warn:before{background:var(--ylw)}.tl.err:before{background:var(--red)}.tl small{color:var(--mut2);font-size:10px}
.toast{position:fixed;bottom:20px;right:20px;background:var(--panel2);border:1px solid var(--grn);border-radius:9px;padding:12px 16px;font-size:12px;box-shadow:var(--sh);z-index:99;display:none;max-width:360px}
.intgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(285px,1fr));gap:12px}
.intcard{background:linear-gradient(160deg,var(--panel),var(--bg2));border:1px solid var(--line);border-radius:10px;padding:13px;cursor:pointer;transition:.15s}.intcard:hover{border-color:var(--cy);transform:translateY(-2px)}
.intcard .ih{display:flex;align-items:center;gap:9px;margin-bottom:7px}.intcard .il{width:34px;height:34px;border-radius:8px;background:var(--chip);display:grid;place-items:center;font-size:16px}.intcard b{font-size:12.5px}.intcard .iflow{font-size:10px;color:var(--cy);margin-top:6px;line-height:1.5}
'''
JS = r'''
function tab(g,id,el){document.querySelectorAll('[data-grp="'+g+'"]').forEach(t=>t.classList.remove('on'));document.querySelectorAll('[data-view="'+g+'"]').forEach(v=>v.classList.remove('on'));if(el)el.classList.add('on');var v=document.getElementById(id);if(v)v.classList.add('on');var m=document.querySelector('.main');if(m)m.scrollTop=0;}
function gotab(id){var t=document.getElementById('t_'+id);if(t)t.click();}
function selRow(el,msg){document.querySelectorAll('tr.sel').forEach(r=>r.classList.remove('sel'));el.classList.add('sel');toast(msg||'Registro selecionado — painel lateral atualizado');}
function toast(m){var t=document.getElementById('toast');t.innerHTML=m;t.style.display='block';clearTimeout(window._tt);window._tt=setTimeout(()=>t.style.display='none',2800);}
function go(u){if(u==='#'){toast('Módulo integrado (mock) — navegação ilustrativa');return;}toast('Abrindo módulo integrado…');setTimeout(()=>location.href=u,450);}
function mode(m,el){document.querySelectorAll('#modesw .ms').forEach(x=>x.classList.remove('on'));el.classList.add('on');var map={'v_dash':'t_dash','v_mapa':'t_mapa','v_esteira':'t_esteira'};var t=document.getElementById(map[m]);if(t)t.click();}
function wstep(n){document.querySelectorAll('.wzpane').forEach(p=>p.style.display='none');document.getElementById('wz'+n).style.display='block';document.querySelectorAll('#wizard .step').forEach((s,i)=>{s.classList.remove('on','done');if(i<n-1)s.classList.add('done');if(i==n-1)s.classList.add('on');});}
function layer(el){var sw=el.querySelector('.sw');if(sw)sw.classList.toggle('off');toast('Camada do mapa alternada');}
'''
