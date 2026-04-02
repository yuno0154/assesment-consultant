import json

with open('all_data_js.txt', encoding='utf-8') as f:
    all_data_js = f.read()
with open('groups_new.json', encoding='utf-8') as f:
    groups_data = json.load(f)
groups_js = json.dumps(groups_data, ensure_ascii=False, separators=(',',':'))

html = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2026학년도 중등 학생평가 종합점검단 (균형편성)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
<style>
:root {
  --primary: #6366f1; --primary-hover: #4f46e5;
  --secondary: #0f172a; --accent: #10b981;
  --bg-canvas: #f8fafc; --bg-card: #ffffff;
  --text-main: #1e293b; --text-muted: #64748b;
  --border: #e2e8f0; --sidebar-width: 280px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
  --radius: 12px;
}
* { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
body { font-family: "Inter","Noto Sans KR",sans-serif; background: var(--bg-canvas); color: var(--text-main); overflow-x: hidden; display: flex; min-height: 100vh; }

aside { width: var(--sidebar-width); background: var(--secondary); color: #fff; padding: 2rem 1.5rem; position: fixed; height: 100vh; left: 0; top: 0; z-index: 100; display: flex; flex-direction: column; box-shadow: 4px 0 24px rgba(0,0,0,0.05); overflow-y: auto; }
.logo { display: flex; align-items: center; gap: 12px; margin-bottom: 2rem; }
.logo-icon { width: 40px; height: 40px; background: linear-gradient(135deg, var(--primary), #a855f7); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; }
.logo-text { font-weight: 700; font-size: 1rem; line-height: 1.3; }
.nav-section-label { font-size: 0.7rem; color: #475569; text-transform: uppercase; letter-spacing: 0.8px; margin: 1.2rem 0 0.5rem 0.5rem; font-weight: 600; }
.nav-menu { list-style: none; display: flex; flex-direction: column; gap: 4px; }
.nav-item { padding: 10px 14px; border-radius: var(--radius); cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 10px; color: #94a3b8; font-weight: 500; font-size: 0.9rem; }
.nav-item:hover { background: rgba(255,255,255,0.05); color: #fff; }
.nav-item.active { background: var(--primary); color: #fff; box-shadow: 0 4px 12px rgba(99,102,241,0.3); }
.nav-item ion-icon { font-size: 1.1rem; flex-shrink: 0; }
.nav-divider { border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 1rem 0; }

main { margin-left: var(--sidebar-width); flex: 1; padding: 2rem 2.5rem; }
header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2rem; }
.header-title h1 { font-size: 1.6rem; font-weight: 700; color: var(--secondary); margin-bottom: 4px; }
.header-title p { color: var(--text-muted); font-size: 0.9rem; }
.header-badge { display: inline-block; background: #dcfce7; color: #166534; font-size: 0.75rem; font-weight: 600; padding: 3px 10px; border-radius: 20px; margin-left: 10px; vertical-align: middle; }
.header-actions { display: flex; gap: 10px; }
.btn { padding: 9px 18px; border-radius: var(--radius); font-weight: 500; cursor: pointer; border: none; display: flex; align-items: center; gap: 7px; transition: all 0.2s; font-size: 0.88rem; font-family: inherit; }
.btn-primary { background: var(--primary); color: #fff; }
.btn-primary:hover { background: var(--primary-hover); transform: translateY(-1px); }
.btn-outline { background: #fff; color: var(--secondary); border: 1px solid var(--border); }
.btn-outline:hover { background: #f1f5f9; }
.btn-green { background: #16a34a; color: #fff; }
.btn-green:hover { background: #15803d; transform: translateY(-1px); }

.stats-grid { display: grid; grid-template-columns: repeat(6,1fr); gap: 14px; margin-bottom: 2rem; }
.stat-card { background: var(--bg-card); padding: 1.25rem; border-radius: var(--radius); border: 1px solid var(--border); text-align: center; transition: transform 0.2s; }
.stat-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }
.stat-card h3 { font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
.stat-card .value { font-size: 1.4rem; font-weight: 700; color: var(--secondary); }

.dashboard-container { background: var(--bg-card); border-radius: var(--radius); border: 1px solid var(--border); box-shadow: var(--shadow-sm); overflow: hidden; }
.toolbar { padding: 1.25rem 1.5rem; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; background: #fafafa; flex-wrap: wrap; gap: 10px; }
.search-container { position: relative; width: 300px; }
.search-container ion-icon { position: absolute; left: 11px; top: 50%; transform: translateY(-50%); color: var(--text-muted); font-size: 1.1rem; }
.search-input { width: 100%; padding: 9px 9px 9px 36px; border-radius: 10px; border: 1px solid var(--border); outline: none; font-size: 0.9rem; transition: border-color 0.2s; font-family: inherit; }
.search-input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(99,102,241,0.1); }
.table-responsive { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
th { padding: 11px 14px; background: #f8fafc; border-bottom: 2px solid var(--border); font-size: 0.78rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.4px; }
th.sortable { cursor: pointer; user-select: none; }
th.sortable:hover { background: #f1f5f9; color: var(--primary); }
th.active-sort { color: var(--primary); background: #eef2ff; }
td { padding: 13px 14px; border-bottom: 1px solid var(--border); }
tr:last-child td { border-bottom: none; }
tr:hover td { background: #f8fafc; }
.hidden-col { display: none !important; }
.category-badge { padding: 3px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 600; display: inline-block; }
.cat-1 { background: #e0f2fe; color: #0369a1; }
.cat-2 { background: #fef9c3; color: #854d0e; }
.cat-3 { background: #dcfce7; color: #166534; }
.cat-4 { background: #fee2e2; color: #991b1b; }
.cat-5 { background: #f3e8ff; color: #6b21a8; }
.cat-6 { background: #ffedd5; color: #9a3412; }
.leader-badge { background: #e53e3e; color: #fff; font-size: 0.65rem; padding: 1px 6px; border-radius: 10px; margin-left: 5px; font-weight: 700; vertical-align: middle; }
.empty-state { padding: 3rem; text-align: center; color: var(--text-muted); }

#view-groups { display: none; }
.groups-controls { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 10px; }
.left-controls { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.school-filter { display: flex; gap: 8px; }
.sf-btn { padding: 7px 18px; border: 2px solid var(--border); border-radius: 20px; background: #fff; cursor: pointer; font-size: 0.84rem; font-family: inherit; transition: all 0.2s; }
.sf-btn.active { background: var(--primary); color: #fff; border-color: var(--primary); }
.sf-btn:hover:not(.active) { border-color: var(--primary); color: var(--primary); }
.view-toggle { display: flex; gap: 6px; }
.vt-btn { padding: 7px 14px; border: 2px solid var(--border); border-radius: 8px; background: #fff; cursor: pointer; font-size: 0.84rem; font-family: inherit; transition: all 0.2s; }
.vt-btn.active { background: var(--primary); color: #fff; border-color: var(--primary); }
.g-section-label { font-size: 1rem; font-weight: 700; color: #1e3a5f; margin: 1.5rem 0 0.75rem; padding-bottom: 7px; border-bottom: 2px solid #2d6a9f; }
.g-section-label.mid { color: #1a4731; border-bottom-color: #2d6a4f; }

.g-table-wrap { background: #fff; border-radius: var(--radius); border: 1px solid var(--border); overflow: hidden; box-shadow: var(--shadow-sm); margin-bottom: 1.5rem; }
.g-table-head { padding: 9px 14px; background: #1e3a5f; color: #fff; font-weight: 700; font-size: 0.9rem; }
.g-table-head.mid { background: #1a4731; }
.g-table-wrap table th { background: #e8f0fe; border-bottom: 2px solid #b8c9e8; color: #1e3a5f; }
.g-num-cell { font-size: 1rem; font-weight: 800; color: #2d6a9f; }
.g-num-cell.mid { color: #2d6a4f; }
.g-leader-row td { background: #fff5f5; }
.g-leader-row:hover td { background: #fed7d7; }

#g-card-view { display: none; }
.cards-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; margin-bottom: 1.5rem; }
.group-card { background: #fff; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.07); overflow: hidden; transition: transform 0.2s, box-shadow 0.2s; }
.group-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.11); }
.card-hdr { padding: 11px 16px; background: linear-gradient(135deg,#1e3a5f,#2d6a9f); color: #fff; display: flex; justify-content: space-between; align-items: center; }
.card-hdr.mid { background: linear-gradient(135deg,#1a4731,#2d6a4f); }
.card-hdr h3 { font-size: 1rem; font-weight: 700; }
.card-hdr-right { display: flex; align-items: center; gap: 8px; }
.card-hdr .cnt { font-size: 0.78rem; opacity: 0.85; }
.card-grp-badges { display: flex; gap: 4px; flex-wrap: wrap; }
.card-grp-dot { font-size: 0.68rem; padding: 1px 6px; border-radius: 10px; font-weight: 700; background: rgba(255,255,255,0.2); }
.m-row { display: flex; align-items: center; padding: 9px 14px; border-bottom: 1px solid #f0f4f8; gap: 10px; }
.m-row:last-child { border-bottom: none; }
.m-row.leader { background: #fff5f5; }
.m-num { width: 22px; height: 22px; border-radius: 50%; background: #e2e8f0; color: #4a5568; font-size: 0.68rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.m-row.leader .m-num { background: #e53e3e; color: #fff; }
.m-info { flex: 1; min-width: 0; }
.m-name { font-weight: 700; font-size: 0.88rem; }
.m-school { font-size: 0.72rem; color: #4a5568; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.m-type { font-size: 0.7rem; color: #718096; }
.m-right { display: flex; flex-direction: column; align-items: flex-end; gap: 3px; flex-shrink: 0; }
.m-subj { font-size: 0.72rem; font-weight: 600; padding: 2px 8px; border-radius: 10px; background: #edf2f7; color: #4a5568; white-space: nowrap; }
.m-grp-badge { font-size: 0.65rem; font-weight: 700; padding: 1px 6px; border-radius: 10px; white-space: nowrap; }
.m-row.leader .m-subj { background: #fed7d7; color: #9b2c2c; }

.grp-badge-1 { background: #e0f2fe; color: #0369a1; }
.grp-badge-2 { background: #fef9c3; color: #854d0e; }
.grp-badge-3 { background: #dcfce7; color: #166534; }
.grp-badge-4 { background: #fee2e2; color: #991b1b; }
.grp-badge-5 { background: #f3e8ff; color: #6b21a8; }
.grp-badge-6 { background: #ffedd5; color: #9a3412; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
.fade-in { animation: fadeIn 0.3s ease forwards; }
::-webkit-scrollbar { width: 7px; }
::-webkit-scrollbar-track { background: var(--bg-canvas); }
::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }

@media print {
  aside, .header-actions, .toolbar, .groups-controls, .stats-grid { display: none !important; }
  main { margin-left: 0 !important; padding: 0 !important; }
  .dashboard-container, .g-table-wrap { border: none !important; box-shadow: none !important; }
  .group-card { break-inside: avoid; }
}
@media (max-width: 900px) {
  aside { width: 220px; }
  main { margin-left: 220px; padding: 1.2rem; }
  .stats-grid { grid-template-columns: repeat(3,1fr); }
}
</style>
</head>
<body>

<aside>
  <div class="logo">
    <div class="logo-icon"><ion-icon name="analytics"></ion-icon></div>
    <div class="logo-text">2026 학생평가<br>종합점검단</div>
  </div>

  <p class="nav-section-label">전체 명단</p>
  <ul class="nav-menu">
    <li class="nav-item active" data-view="list" data-cat="all">
      <ion-icon name="grid-outline"></ion-icon><span>전체 보기</span>
    </li>
    <li class="nav-item" data-view="list" data-cat="1">
      <ion-icon name="bookmark-outline"></ion-icon><span>1그룹</span>
    </li>
    <li class="nav-item" data-view="list" data-cat="2">
      <ion-icon name="document-text-outline"></ion-icon><span>2그룹</span>
    </li>
    <li class="nav-item" data-view="list" data-cat="3">
      <ion-icon name="reader-outline"></ion-icon><span>3그룹</span>
    </li>
    <li class="nav-item" data-view="list" data-cat="4">
      <ion-icon name="briefcase-outline"></ion-icon><span>4그룹</span>
    </li>
    <li class="nav-item" data-view="list" data-cat="5">
      <ion-icon name="ribbon-outline"></ion-icon><span>5그룹</span>
    </li>
    <li class="nav-item" data-view="list" data-cat="6">
      <ion-icon name="options-outline"></ion-icon><span>6그룹</span>
    </li>
  </ul>

  <hr class="nav-divider">
  <p class="nav-section-label">모둠 편성 (균형)</p>
  <ul class="nav-menu">
    <li class="nav-item" data-view="groups">
      <ion-icon name="people-outline"></ion-icon><span>모둠 편성 결과</span>
    </li>
  </ul>
</aside>

<main>
  <header>
    <div class="header-title">
      <h1>2026학년도 중등 학생평가 종합점검단 <span class="header-badge">균형편성</span></h1>
      <p id="current-date"></p>
    </div>
    <div class="header-actions">
      <button class="btn btn-outline" onclick="window.print()">
        <ion-icon name="print-outline"></ion-icon> 인쇄
      </button>
    </div>
  </header>

  <!-- LIST VIEW -->
  <div id="view-list">
    <section class="stats-grid">
      <div class="stat-card"><h3>전체</h3><div class="value" id="stat-all">0</div></div>
      <div class="stat-card"><h3>1그룹</h3><div class="value" id="stat-1">0</div></div>
      <div class="stat-card"><h3>2그룹</h3><div class="value" id="stat-2">0</div></div>
      <div class="stat-card"><h3>3그룹</h3><div class="value" id="stat-3">0</div></div>
      <div class="stat-card"><h3>4그룹</h3><div class="value" id="stat-4">0</div></div>
      <div class="stat-card"><h3>5/6그룹</h3><div class="value" id="stat-56">0</div></div>
    </section>
    <div class="dashboard-container">
      <div class="toolbar">
        <div class="search-container">
          <ion-icon name="search-outline"></ion-icon>
          <input type="text" class="search-input" id="search-input" placeholder="이름 또는 학교 검색...">
        </div>
        <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
          <button class="btn btn-outline" id="remarks-btn" onclick="toggleRemarks()">
            <ion-icon name="document-text-outline"></ion-icon> 비고 표시
          </button>
          <span style="font-size:0.82rem;color:var(--text-muted);" id="table-count"></span>
        </div>
      </div>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th class="sortable" onclick="sortBy(\'id\')">순번</th>
              <th class="sortable" onclick="sortBy(\'name\')">이름</th>
              <th class="sortable" onclick="sortBy(\'org\')">학교</th>
              <th class="sortable" onclick="sortBy(\'pos\')">구분</th>
              <th class="sortable" onclick="sortBy(\'subject\')">과목</th>
              <th class="sortable" onclick="sortBy(\'class\')">그룹</th>
              <th class="remarks-col hidden-col">비고</th>
            </tr>
          </thead>
          <tbody id="student-body"></tbody>
        </table>
        <div id="empty-state" class="empty-state" style="display:none;"><p>검색 결과가 없습니다.</p></div>
      </div>
    </div>
  </div>

  <!-- GROUPS VIEW -->
  <div id="view-groups" style="display:none;">
    <div class="groups-controls">
      <div class="left-controls">
        <div class="school-filter">
          <button class="sf-btn active" onclick="setSchoolFilter(\'all\',this)">전체</button>
          <button class="sf-btn" onclick="setSchoolFilter(\'고등학교\',this)">고등학교</button>
          <button class="sf-btn" onclick="setSchoolFilter(\'중학교\',this)">중학교</button>
        </div>
        <div class="view-toggle">
          <button class="vt-btn active" onclick="setGroupView(\'table\',this)">&#9776; 표 보기</button>
          <button class="vt-btn" onclick="setGroupView(\'card\',this)">&#9638; 카드 보기</button>
        </div>
      </div>
      <button class="btn btn-green" onclick="exportExcel()">
        <ion-icon name="download-outline"></ion-icon> 엑셀 다운로드
      </button>
    </div>

    <!-- Table View -->
    <div id="g-table-view">
      <div id="g-high-section">
        <p class="g-section-label">&#x1F3EB; 고등학교 모둠 (1~12모둠)</p>
        <div class="g-table-wrap">
          <div class="g-table-head">고등학교</div>
          <table>
            <thead><tr><th>모둠</th><th>순</th><th>이름</th><th>학교명</th><th>구분</th><th>과목</th><th>그룹</th><th>팀장</th></tr></thead>
            <tbody id="gtbody-high"></tbody>
          </table>
        </div>
      </div>
      <div id="g-mid-section">
        <p class="g-section-label mid">&#x1F3EB; 중학교 모둠 (13~20모둠)</p>
        <div class="g-table-wrap">
          <div class="g-table-head mid">중학교</div>
          <table>
            <thead><tr><th>모둠</th><th>순</th><th>이름</th><th>학교명</th><th>구분</th><th>과목</th><th>그룹</th><th>팀장</th></tr></thead>
            <tbody id="gtbody-mid"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Card View -->
    <div id="g-card-view" style="display:none;">
      <div id="g-high-card-section">
        <p class="g-section-label">&#x1F3EB; 고등학교 모둠 (1~12모둠)</p>
        <div class="cards-grid" id="cards-high"></div>
      </div>
      <div id="g-mid-card-section">
        <p class="g-section-label mid">&#x1F3EB; 중학교 모둠 (13~20모둠)</p>
        <div class="cards-grid" id="cards-mid"></div>
      </div>
    </div>
  </div>
</main>

<script>
const allData = ''' + all_data_js + ''';
const groups = ''' + groups_js + ''';

const GRP_LABEL = ["","1그룹","2그룹","3그룹","4그룹","5그룹","6그룹"];
const GRP_STYLE = ["","background:#e0f2fe;color:#0369a1","background:#fef9c3;color:#854d0e","background:#dcfce7;color:#166534","background:#fee2e2;color:#991b1b","background:#f3e8ff;color:#6b21a8","background:#ffedd5;color:#9a3412"];

document.getElementById("current-date").textContent = new Date().toLocaleDateString("ko-KR",{year:"numeric",month:"long",day:"numeric",weekday:"long"});

let currentCat="all", sortCol="class", sortDir="asc", remarksVisible=false;

function updateStats(){
  document.getElementById("stat-all").textContent=allData.length;
  for(let i=1;i<=6;i++){const el=document.getElementById("stat-"+i);if(el)el.textContent=allData.filter(d=>d.class===i).length;}
  document.getElementById("stat-56").textContent=allData.filter(d=>d.class===5||d.class===6).length;
}

function renderTable(){
  const q=document.getElementById("search-input").value.toLowerCase();
  const body=document.getElementById("student-body");
  let data=allData.slice();
  if(currentCat!=="all") data=data.filter(d=>d.class===parseInt(currentCat));
  if(q) data=data.filter(d=>d.name.toLowerCase().includes(q)||d.org.toLowerCase().includes(q));
  data.sort((a,b)=>{
    let va=a[sortCol]??999, vb=b[sortCol]??999;
    return sortDir==="asc"?(va<vb?-1:va>vb?1:0):(va<vb?1:va>vb?-1:0);
  });
  document.getElementById("empty-state").style.display=data.length===0?"block":"none";
  const rmCls=remarksVisible?"":" hidden-col";
  body.innerHTML=data.map(d=>{
    const badge=`<span class="category-badge cat-${d.class}">${d.class?GRP_LABEL[d.class]:"미분류"}</span>`;
    const ldr=d.is_leader?`<span class="leader-badge">팀장</span>`:"";
    return `<tr class="fade-in">
      <td style="color:#94a3b8;font-weight:500;">#${d.id}</td>
      <td style="font-weight:600;">${d.name}${ldr}</td>
      <td>${d.org}</td><td>${d.pos}</td><td>${d.subject}</td>
      <td>${badge}</td>
      <td class="remarks-col${rmCls}" style="font-size:0.78rem;color:#64748b;max-width:180px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${d.remarks||""}</td>
    </tr>`;
  }).join("");
  document.getElementById("table-count").textContent=`총 ${data.length}명 표시 중`;
  document.querySelectorAll("th.remarks-col").forEach(th=>{th.className="remarks-col"+rmCls;});
}

function toggleRemarks(){
  remarksVisible=!remarksVisible;
  document.getElementById("remarks-btn").className=remarksVisible?"btn btn-primary":"btn btn-outline";
  renderTable();
}
function sortBy(col){sortDir=(sortCol===col)?(sortDir==="asc"?"desc":"asc"):"asc";sortCol=col;renderTable();}
document.getElementById("search-input").addEventListener("input",renderTable);

document.querySelectorAll(".nav-item").forEach(item=>{
  item.addEventListener("click",()=>{
    document.querySelectorAll(".nav-item").forEach(i=>i.classList.remove("active"));
    item.classList.add("active");
    const v=item.getAttribute("data-view");
    if(v==="groups"){
      document.getElementById("view-list").style.display="none";
      document.getElementById("view-groups").style.display="block";
    } else {
      document.getElementById("view-list").style.display="block";
      document.getElementById("view-groups").style.display="none";
      currentCat=item.getAttribute("data-cat")||"all";
      renderTable();
    }
  });
});

// GROUP TABLE
function buildGroupTable(){
  const highBody=document.getElementById("gtbody-high");
  const midBody=document.getElementById("gtbody-mid");
  highBody.innerHTML=""; midBody.innerHTML="";
  groups.forEach(g=>{
    const isMid=g.school_level==="중학교";
    const body=isMid?midBody:highBody;
    const numCls=isMid?"g-num-cell mid":"g-num-cell";
    g.members.forEach((m,idx)=>{
      const tr=document.createElement("tr");
      tr.dataset.level=g.school_level;
      if(m.is_leader) tr.className="g-leader-row";
      const grpBadge=m.main_grp?`<span class="category-badge cat-${m.main_grp}">${GRP_LABEL[m.main_grp]}</span>`:"";
      const typeBadge=m.school_type.includes("수석")
        ?`<span class="category-badge" style="background:#fef3c7;color:#92400e;">수석교사</span>`
        :`<span class="category-badge" style="background:#e0f2fe;color:#0c4a6e;">교사</span>`;
      const ldrBadge=m.is_leader?`<span class="leader-badge">팀장</span>`:"";
      let html="";
      if(idx===0) html+=`<td rowspan="${g.members.length}" class="${numCls}">${g.group_num}모둠</td>`;
      html+=`<td style="color:#94a3b8;">${idx+1}</td>`;
      html+=`<td style="font-weight:600;">${m.name}${ldrBadge}</td>`;
      html+=`<td>${m.school}</td><td>${typeBadge}</td><td>${m.subject}</td>`;
      html+=`<td>${grpBadge}</td><td>${ldrBadge}</td>`;
      tr.innerHTML=html;
      body.appendChild(tr);
    });
  });
}

// GROUP CARDS
function buildGroupCards(){
  const highGrid=document.getElementById("cards-high");
  const midGrid=document.getElementById("cards-mid");
  highGrid.innerHTML=""; midGrid.innerHTML="";
  groups.forEach(g=>{
    const isMid=g.school_level==="중학교";
    const grid=isMid?midGrid:highGrid;
    const card=document.createElement("div");
    card.className="group-card"; card.dataset.level=g.school_level;
    const hdrCls=isMid?"card-hdr mid":"card-hdr";

    // 카드 헤더에 그룹 분포 뱃지
    const grpCounts={};
    g.members.forEach(m=>{if(m.main_grp>=2)grpCounts[m.main_grp]=(grpCounts[m.main_grp]||0)+1;});
    const grpBadgesHtml=Object.entries(grpCounts).sort().map(([g,c])=>
      `<span class="card-grp-dot">${GRP_LABEL[g]}×${c}</span>`
    ).join("");

    const membersHtml=g.members.map((m,idx)=>{
      const ldrCls=m.is_leader?" leader":"";
      const typeLabel=m.school_type.includes("수석")?"수석교사":"교사";
      const ldrMark=m.is_leader?` <span style="color:#e53e3e;font-size:0.72rem;">&#9733;팀장</span>`:"";
      const grpBadge=m.main_grp?`<span class="m-grp-badge grp-badge-${m.main_grp}">${GRP_LABEL[m.main_grp]}</span>`:"";
      return `<div class="m-row${ldrCls}">
        <div class="m-num">${idx+1}</div>
        <div class="m-info">
          <div class="m-name">${m.name}${ldrMark}</div>
          <div class="m-school" title="${m.school}">${m.school}</div>
          <div class="m-type">${typeLabel}</div>
        </div>
        <div class="m-right">
          <div class="m-subj">${m.subject}</div>
          ${grpBadge}
        </div>
      </div>`;
    }).join("");

    card.innerHTML=`<div class="${hdrCls}">
      <h3>${g.group_num}모둠</h3>
      <div class="card-hdr-right">
        <div class="card-grp-badges">${grpBadgesHtml}</div>
        <span class="cnt">${g.members.length}명</span>
      </div>
    </div><div class="card-body">${membersHtml}</div>`;
    grid.appendChild(card);
  });
}

let schoolFilter="all", groupViewMode="table";
function setSchoolFilter(level,btn){
  schoolFilter=level;
  document.querySelectorAll(".sf-btn").forEach(b=>b.classList.remove("active"));
  btn.classList.add("active");
  const showHigh=level==="all"||level==="고등학교";
  const showMid=level==="all"||level==="중학교";
  ["g-high-section","g-high-card-section"].forEach(id=>{document.getElementById(id).style.display=showHigh?"":"none";});
  ["g-mid-section","g-mid-card-section"].forEach(id=>{document.getElementById(id).style.display=showMid?"":"none";});
}
function setGroupView(mode,btn){
  groupViewMode=mode;
  document.querySelectorAll(".vt-btn").forEach(b=>b.classList.remove("active"));
  btn.classList.add("active");
  document.getElementById("g-table-view").style.display=mode==="table"?"block":"none";
  document.getElementById("g-card-view").style.display=mode==="card"?"block":"none";
}

// EXCEL EXPORT
function exportExcel(){
  const wb=XLSX.utils.book_new();
  const all_rows=[];

  groups.forEach(g=>{
    g.members.forEach((m,idx)=>{
      all_rows.push({
        "학교급": g.school_level,
        "모둠번호": g.group_num+"모둠",
        "순번": idx+1,
        "이름": m.name,
        "학교명": m.school,
        "구분": m.school_type,
        "과목": m.subject,
        "그룹": m.main_grp?GRP_LABEL[m.main_grp]:"",
        "팀장": m.is_leader?"팀장":""
      });
    });
    // 빈 행 구분
    all_rows.push({});
  });

  const ws=XLSX.utils.json_to_sheet(all_rows);

  // 열 너비
  ws["!cols"]=[
    {wch:8},{wch:10},{wch:5},{wch:10},{wch:24},{wch:8},{wch:12},{wch:8},{wch:6}
  ];

  XLSX.utils.book_append_sheet(wb,ws,"모둠편성");

  // 시트2: 고등학교만
  const high_rows=[];
  groups.filter(g=>g.school_level==="고등학교").forEach(g=>{
    g.members.forEach((m,idx)=>{
      high_rows.push({"모둠":g.group_num+"모둠","순번":idx+1,"이름":m.name,"학교명":m.school,"구분":m.school_type,"과목":m.subject,"그룹":m.main_grp?GRP_LABEL[m.main_grp]:"","팀장":m.is_leader?"팀장":""});
    });
    high_rows.push({});
  });
  const ws2=XLSX.utils.json_to_sheet(high_rows);
  ws2["!cols"]=[{wch:10},{wch:5},{wch:10},{wch:24},{wch:8},{wch:12},{wch:8},{wch:6}];
  XLSX.utils.book_append_sheet(wb,ws2,"고등학교모둠");

  // 시트3: 중학교만
  const mid_rows=[];
  groups.filter(g=>g.school_level==="중학교").forEach(g=>{
    g.members.forEach((m,idx)=>{
      mid_rows.push({"모둠":g.group_num+"모둠","순번":idx+1,"이름":m.name,"학교명":m.school,"구분":m.school_type,"과목":m.subject,"그룹":m.main_grp?GRP_LABEL[m.main_grp]:"","팀장":m.is_leader?"팀장":""});
    });
    mid_rows.push({});
  });
  const ws3=XLSX.utils.json_to_sheet(mid_rows);
  ws3["!cols"]=[{wch:10},{wch:5},{wch:10},{wch:24},{wch:8},{wch:12},{wch:8},{wch:6}];
  XLSX.utils.book_append_sheet(wb,ws3,"중학교모둠");

  XLSX.writeFile(wb,"2026_학생평가종합점검단_모둠편성.xlsx");
}

updateStats(); renderTable(); buildGroupTable(); buildGroupCards();
</script>
</body>
</html>'''

with open('index2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done:', len(html), 'chars')
