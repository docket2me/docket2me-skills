const copyButtons = document.querySelectorAll("[data-copy-target]");

async function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text);
    return;
  }

  const textArea = document.createElement("textarea");
  textArea.value = text;
  textArea.setAttribute("readonly", "");
  textArea.style.position = "fixed";
  textArea.style.left = "-9999px";
  document.body.appendChild(textArea);
  textArea.select();
  document.execCommand("copy");
  textArea.remove();
}

copyButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    const target = document.getElementById(button.dataset.copyTarget);
    if (!target) return;

    const originalText = button.textContent;
    try {
      await copyText(target.textContent.trim());
      button.textContent = "Copied";
      button.classList.add("copied");
      window.setTimeout(() => {
        button.textContent = originalText;
        button.classList.remove("copied");
      }, 1700);
    } catch {
      button.textContent = "Select text";
      window.setTimeout(() => {
        button.textContent = originalText;
      }, 1700);
    }
  });
});
