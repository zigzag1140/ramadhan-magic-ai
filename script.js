const API_BASE = "https://ramadanmagic-ai-mienccnecg.cn-hangzhou.fcapp.run";

async function generateMagic() {
  const msg = document.getElementById("userInput").value;
  if (!msg) return alert("Isi curhatanmu dulu!");

  const btn = document.getElementById("btnMagic");
  const resultArea = document.getElementById("resultArea");

  btn.innerText = "Membuat Keajaiban...";
  btn.disabled = true;

  try {
    const res = await fetch(`${API_BASE}/magic`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ msg }),
    });

    const data = await res.json();
    if (data.error) throw new Error(data.error);

    document.getElementById("captionText").innerText = `"${data.caption}"`;
    document.getElementById("imageResult").src = data.image_url;

    resultArea.classList.remove("hidden");
    resultArea.scrollIntoView({ behavior: "smooth" });
  } catch (err) {
    console.error("Magic Error:", err);
    alert("Waduh, AI-nya lagi buka puasa. Coba lagi ya!");
  } finally {
    btn.innerText = "Create Magic ✨";
    btn.disabled = false;
  }
}

async function downloadMedia() {
  const img = document.getElementById("imageResult");
  const url = img.src;

  if (!url) return;

  try {
    const response = await fetch(url);
    const blob = await response.blob();
    const blobUrl = window.URL.createObjectURL(blob);
    const a = document.createElement("a");

    a.href = blobUrl;
    a.download = `RamadanMagic_${Date.now()}.png`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    window.URL.revokeObjectURL(blobUrl);
  } catch (e) {
    window.open(url, "_blank");
  }
}
