async function uploadFile() {
  const fileInput = document.getElementById('uploadInput');
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  const response = await fetch("/upload", {
    method: "POST",
    body: formData
  });
  alert(await response.text());
}

async function sync() {
  const response = await fetch("/sync", {
    method: "POST"
  });
  alert(await response.text());
}
