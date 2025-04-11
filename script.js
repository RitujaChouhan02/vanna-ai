async function ask() {
    const input = document.getElementById("question");
    const question = input.value.trim();
    if (!question) return;
  
    const chatWindow = document.getElementById("chat-window");
    chatWindow.innerHTML = ''; // Clear previous results
  
    appendMessage("You asked:", question);
    input.value = "";
  
    try {
      const res = await fetch("http://localhost:8000/generate-sql", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      });
  
      const data = await res.json();
  
      if (data.sql) {
        appendMessage("🧠 Generated SQL:", data.sql);
      }
  
      if (data.result && data.result.length > 0) {
        appendTable(data.result);
      } else {
        appendMessage("📊 Result:", "No results found.");
      }
    } catch (err) {
      appendMessage("Error:", err.message);
    }
  }
  
  function appendMessage(title, content) {
    const chatWindow = document.getElementById("chat-window");
    const msgDiv = document.createElement("div");
    msgDiv.className = "message";
  
    const titleEl = document.createElement("div");
    titleEl.className = "message-title";
    titleEl.innerText = title;
  
    const contentEl = document.createElement("pre");
    contentEl.innerText = content;
  
    msgDiv.appendChild(titleEl);
    msgDiv.appendChild(contentEl);
    chatWindow.appendChild(msgDiv);
  }
  
  function appendTable(rows) {
    const chatWindow = document.getElementById("chat-window");
    const container = document.createElement("div");
    container.className = "message";
  
    const titleEl = document.createElement("div");
    titleEl.className = "message-title";
    titleEl.innerText = "📊 Result:";
  
    const table = document.createElement("table");
    const headerRow = table.insertRow();
    Object.keys(rows[0]).forEach(key => {
      const th = document.createElement("th");
      th.textContent = key;
      headerRow.appendChild(th);
    });
  
    rows.forEach(row => {
      const tr = table.insertRow();
      Object.values(row).forEach(value => {
        const td = tr.insertCell();
        td.textContent = value;
      });
    });
  
    container.appendChild(titleEl);
    container.appendChild(table);
    chatWindow.appendChild(container);
  }
  