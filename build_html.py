import json

with open('groups_js.txt', encoding='utf-8') as f:
    js_data = f.read()

html = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2026 학생평가 종합점검단 모둠 편성</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Malgun Gothic", sans-serif; background: #f0f4f8; color: #1a202c; }

header {
  background: linear-gradient(135deg, #1e3a5f 0%, #2d6a9f 100%);
  color: white; padding: 20px 30px; text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
header h1 { font-size: 1.5rem; font-weight: 700; margin-bottom: 4px; }
header p { font-size: 0.88rem; opacity: 0.85; }

.controls {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 24px; background: white;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 100;
  flex-wrap: wrap; gap: 10px;
}
.filter-group { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.filter-btn {
  padding: 6px 16px; border: 2px solid #cbd5e0; border-radius: 20px;
  background: white; cursor: pointer; font-size: 0.84rem; transition: all 0.2s;
  font-family: inherit;
}
.filter-btn.active { background: #2d6a9f; color: white; border-color: #2d6a9f; }
.filter-btn:hover:not(.active) { border-color: #2d6a9f; color: #2d6a9f; }

.view-toggle { display: flex; gap: 6px; }
.view-btn {
  padding: 6px 14px; border: 2px solid #cbd5e0; border-radius: 8px;
  background: white; cursor: pointer; font-size: 0.84rem; transition: all 0.2s;
  font-family: inherit;
}
.view-btn.active { background: #2d6a9f; color: white; border-color: #2d6a9f; }

.main { padding: 20px 24px; max-width: 1600px; margin: 0 auto; }

/* TABLE VIEW */
.section-block { margin-bottom: 28px; }
.section-header {
  background: #1e3a5f; color: white; padding: 10px 16px;
  font-size: 0.95rem; font-weight: 700;
  border-radius: 8px 8px 0 0;
}
.section-header.middle { background: #1a4731; }
table {
  width: 100%; border-collapse: collapse; background: white;
  border-radius: 0 0 8px 8px; overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
thead tr { background: #e8f0fe; }
th {
  padding: 9px 10px; font-size: 0.78rem; text-align: center;
  border-bottom: 2px solid #b8c9e8; white-space: nowrap;
}
td {
  padding: 7px 10px; font-size: 0.8rem; border-bottom: 1px solid #edf2f7;
  text-align: center; vertical-align: middle;
}
tr:last-child td { border-bottom: none; }
tr:hover td { background: #f7fafc; }
.leader-row td { background: #fff5f5; }
.leader-row:hover td { background: #fed7d7; }
.leader-badge {
  display: inline-block; background: #e53e3e; color: white;
  font-size: 0.68rem; padding: 1px 6px; border-radius: 10px;
  margin-left: 4px; vertical-align: middle; font-weight: 700;
}
.badge-master { background: #fef3c7; color: #92400e; padding: 2px 7px; border-radius: 10px; font-size: 0.72rem; font-weight: 600; }
.badge-teacher { background: #e0f2fe; color: #0c4a6e; padding: 2px 7px; border-radius: 10px; font-size: 0.72rem; font-weight: 600; }
.group-num-cell { font-size: 1rem; font-weight: 800; color: #2d6a9f; }
.group-num-cell.middle { color: #2d6a4f; }

/* CARD VIEW */
#card-view { display: none; }
.section-title {
  font-size: 1.1rem; font-weight: 800; color: #1e3a5f;
  margin: 20px 0 12px; padding-bottom: 8px;
  border-bottom: 3px solid #2d6a9f;
}
.section-title.middle { color: #1a4731; border-bottom-color: #2d6a4f; }
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
.group-card {
  background: white; border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  overflow: hidden; transition: transform 0.2s, box-shadow 0.2s;
}
.group-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.12); }
.card-header {
  padding: 11px 16px;
  background: linear-gradient(135deg, #1e3a5f, #2d6a9f);
  color: white; display: flex; justify-content: space-between; align-items: center;
}
.card-header.middle { background: linear-gradient(135deg, #1a4731, #2d6a4f); }
.card-header h3 { font-size: 1rem; font-weight: 700; }
.card-header .count { font-size: 0.78rem; opacity: 0.85; }
.member-row {
  display: flex; align-items: center; padding: 9px 14px;
  border-bottom: 1px solid #f0f4f8; gap: 10px;
}
.member-row:last-child { border-bottom: none; }
.member-row.leader { background: #fff5f5; }
.member-num {
  width: 22px; height: 22px; border-radius: 50%;
  background: #e2e8f0; color: #4a5568;
  font-size: 0.7rem; font-weight: 700;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.member-row.leader .member-num { background: #e53e3e; color: white; }
.member-info { flex: 1; min-width: 0; }
.member-name { font-weight: 700; font-size: 0.88rem; }
.member-school { font-size: 0.72rem; color: #4a5568; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.member-details { font-size: 0.7rem; color: #718096; margin-top: 1px; }
.member-subject {
  font-size: 0.72rem; font-weight: 600; padding: 2px 8px;
  border-radius: 10px; background: #edf2f7; color: #4a5568;
  white-space: nowrap; flex-shrink: 0;
}
.member-row.leader .member-subject { background: #fed7d7; color: #9b2c2c; }

.hidden { display: none !important; }

@media (max-width: 700px) {
  header h1 { font-size: 1.1rem; }
  .main { padding: 12px; }
  .cards-grid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<header>
  <h1>2026학년도 학생평가 종합점검단 모둠 편성</h1>
  <p>고등학교 12모둠 &middot; 중학교 8모둠 &middot; 총 20모둠 | &#9733; 표시: 팀장</p>
</header>

<div class="controls">
  <div class="filter-group">
    <span style="font-size:0.84rem;font-weight:600;color:#4a5568;">학교급:</span>
    <button class="filter-btn active" onclick="setFilter('all',this)">전체</button>
    <button class="filter-btn" onclick="setFilter('고등학교',this)">고등학교</button>
    <button class="filter-btn" onclick="setFilter('중학교',this)">중학교</button>
  </div>
  <div class="view-toggle">
    <button class="view-btn active" onclick="setView('table',this)">&#9776; 표 보기</button>
    <button class="view-btn" onclick="setView('card',this)">&#9638; 카드 보기</button>
  </div>
</div>

<div class="main">
  <!-- TABLE VIEW -->
  <div id="table-view">
    <div class="section-block" id="tbl-high">
      <div class="section-header">&#x1F3EB; 고등학교 모둠 (1~12모둠)</div>
      <table>
        <thead>
          <tr><th>모둠</th><th>순</th><th>이름</th><th>학교명</th><th>구분</th><th>과목</th><th>연락처</th><th>비고</th></tr>
        </thead>
        <tbody id="tbody-high"></tbody>
      </table>
    </div>
    <div class="section-block" id="tbl-mid">
      <div class="section-header middle">&#x1F3EB; 중학교 모둠 (13~20모둠)</div>
      <table>
        <thead>
          <tr><th>모둠</th><th>순</th><th>이름</th><th>학교명</th><th>구분</th><th>과목</th><th>연락처</th><th>비고</th></tr>
        </thead>
        <tbody id="tbody-mid"></tbody>
      </table>
    </div>
  </div>

  <!-- CARD VIEW -->
  <div id="card-view">
    <div class="section-title" id="ct-high">&#x1F3EB; 고등학교 모둠 (1~12모둠)</div>
    <div class="cards-grid" id="cg-high"></div>
    <div class="section-title middle" id="ct-mid">&#x1F3EB; 중학교 모둠 (13~20모둠)</div>
    <div class="cards-grid" id="cg-mid"></div>
  </div>
</div>

<script>
const groups = ''' + js_data + ''';

function buildLeaderRemarks(m) {
  let parts = [];
  if (m.is_leader) parts.push("팀장");
  if (m.remarks) parts.push(m.remarks);
  return parts.join(", ");
}

function buildTable() {
  const highBody = document.getElementById("tbody-high");
  const midBody = document.getElementById("tbody-mid");

  groups.forEach(function(g) {
    const isMiddle = g.school_level === "중학교";
    const body = isMiddle ? midBody : highBody;
    const numClass = isMiddle ? "group-num-cell middle" : "group-num-cell";

    g.members.forEach(function(m, idx) {
      const tr = document.createElement("tr");
      tr.dataset.level = g.school_level;
      if (m.is_leader) tr.className = "leader-row";

      const leaderBadge = m.is_leader ? '<span class="leader-badge">팀장</span>' : "";
      const typeBadge = m.school_type.includes("수석")
        ? '<span class="badge-master">수석교사</span>'
        : '<span class="badge-teacher">교사</span>';

      let remarks = [];
      if (m.is_leader) remarks.push("팀장");
      if (m.remarks) remarks.push(m.remarks);

      let html = "";
      if (idx === 0) {
        html += '<td rowspan="' + g.members.length + '" class="' + numClass + '">' + g.group_num + "모둠</td>";
      }
      html += "<td>" + (idx + 1) + "</td>";
      html += "<td>" + m.name + leaderBadge + "</td>";
      html += '<td style="text-align:left">' + m.school + "</td>";
      html += "<td>" + typeBadge + "</td>";
      html += "<td>" + m.subject + "</td>";
      html += "<td>" + m.phone + "</td>";
      html += '<td style="text-align:left;font-size:0.73rem;color:#4a5568">' + remarks.join(", ") + "</td>";
      tr.innerHTML = html;
      body.appendChild(tr);
    });
  });
}

function buildCards() {
  const highGrid = document.getElementById("cg-high");
  const midGrid = document.getElementById("cg-mid");

  groups.forEach(function(g) {
    const isMiddle = g.school_level === "중학교";
    const grid = isMiddle ? midGrid : highGrid;

    const card = document.createElement("div");
    card.className = "group-card";
    card.dataset.level = g.school_level;

    const headerClass = isMiddle ? "card-header middle" : "card-header";

    let membersHtml = g.members.map(function(m, idx) {
      const leaderClass = m.is_leader ? " leader" : "";
      const typeLabel = m.school_type.includes("수석") ? "수석교사" : "교사";
      const leaderMark = m.is_leader ? ' <span style="color:#e53e3e;font-size:0.73rem">&#9733;팀장</span>' : "";
      const shortRemarks = m.remarks ? (m.remarks.length > 28 ? m.remarks.substring(0, 28) + "..." : m.remarks) : "";
      const detailText = shortRemarks ? typeLabel + " &middot; " + shortRemarks : typeLabel;
      return '<div class="member-row' + leaderClass + '">' +
        '<div class="member-num">' + (idx + 1) + "</div>" +
        '<div class="member-info">' +
          '<div class="member-name">' + m.name + leaderMark + "</div>" +
          '<div class="member-school" title="' + m.school + '">' + m.school + "</div>" +
          '<div class="member-details">' + detailText + "</div>" +
        "</div>" +
        '<div class="member-subject">' + m.subject + "</div>" +
        "</div>";
    }).join("");

    card.innerHTML =
      '<div class="' + headerClass + '">' +
        "<h3>" + g.group_num + "모둠</h3>" +
        '<span class="count">' + g.members.length + "명</span>" +
      "</div>" +
      '<div class="card-body">' + membersHtml + "</div>";

    grid.appendChild(card);
  });
}

let currentFilter = "all";

function setFilter(level, btn) {
  currentFilter = level;
  document.querySelectorAll(".filter-btn").forEach(function(b) { b.classList.remove("active"); });
  btn.classList.add("active");
  applyFilter();
}

function applyFilter() {
  const showHigh = currentFilter === "all" || currentFilter === "고등학교";
  const showMid = currentFilter === "all" || currentFilter === "중학교";

  document.getElementById("tbl-high").style.display = showHigh ? "" : "none";
  document.getElementById("tbl-mid").style.display = showMid ? "" : "none";
  document.getElementById("ct-high").style.display = showHigh ? "" : "none";
  document.getElementById("cg-high").style.display = showHigh ? "" : "none";
  document.getElementById("ct-mid").style.display = showMid ? "" : "none";
  document.getElementById("cg-mid").style.display = showMid ? "" : "none";
}

function setView(view, btn) {
  document.querySelectorAll(".view-btn").forEach(function(b) { b.classList.remove("active"); });
  btn.classList.add("active");
  if (view === "table") {
    document.getElementById("table-view").style.display = "";
    document.getElementById("card-view").style.display = "none";
  } else {
    document.getElementById("table-view").style.display = "none";
    document.getElementById("card-view").style.display = "";
  }
}

buildTable();
buildCards();
</script>
</body>
</html>'''

with open('모둠편성.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done:', len(html), 'chars')
