const showToast = (icon, title) => {
  const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
  })

  Toast.fire({
    icon: icon,
    title: title
  })
}

const checkboxes = document.querySelectorAll(".todo-check")

checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", async () => {
    const toggleUrl = checkbox.dataset.url
    const li = checkbox.closest("li")
    const statusSpan = li.querySelector(".todo-status")
    const todoName = li.querySelector("strong")
    const todoDescription = li.querySelector("p.text-sm")

    try {
      const response = await fetch(toggleUrl, {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"), 
        },
      })
      
      if (!response.ok) {
        checkbox.checked = !checkbox.checked
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json();

      if (data.success) {
          const isDone = data.is_done

          statusSpan.textContent = isDone ? "Completada ✅" : "Pendiente ⏳"

          if (isDone) {
            todoName.classList.add("line-through", "text-gray-400")
            todoName.classList.remove("text-gray-800")

            todoDescription.classList.add("line-through", "text-gray-400")
            todoDescription.classList.remove("text-gray-500")

            statusSpan.classList.add("bg-green-100", "text-green-700")
            statusSpan.classList.remove("bg-yellow-100", "text-yellow-700")

            showToast('success', 'Tarea Completada 🎉')
          } else {
            todoName.classList.remove("line-through", "text-gray-400");
            todoName.classList.add("text-gray-800");

            todoDescription.classList.remove("line-through", "text-gray-400");
            todoDescription.classList.add("text-gray-500");

            statusSpan.classList.remove("bg-green-100", "text-green-700");
            statusSpan.classList.add("bg-yellow-100", "text-yellow-700");

            showToast('info', 'Tarea marcada como Pendiente ✍️');
          }
        } else {
          checkbox.checked = !checkbox.checked
          showToast('error', 'Error al actualizar')
        }
    } catch (error) {
      checkbox.checked = !checkbox.checked
      showToast('error', 'Error de conexión. Intenta de nuevo.')
    }
  })
})

function getCookie(name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";")
    for (let cookie of cookies) {
      cookie = cookie.trim()
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}