document.addEventListener("DOMContentLoaded", function () {
  const stars = document.querySelectorAll(".star");
  const ratingInput = document.getElementById("rating-value");
  const reviewForm = document.getElementById("review-form");
  const reviewList = document.getElementById("reviews-list");

  let selectedRating = 0; // Store the rating value

  // Star Rating Click
  stars.forEach((star) => {
    star.addEventListener("mouseover", function () {
      highlightStars(this.getAttribute("data-value"));
    });
    star.addEventListener("mouseout", function () {
      highlightStars(selectedRating);
    });
    star.addEventListener("click", function () {
      selectedRating = this.getAttribute("data-value");
      ratingInput.value = selectedRating;
      highlightStars(selectedRating);
    });
  });

  function highlightStars(value) {
    stars.forEach((star) => {
      star.classList.toggle(
        "selected",
        star.getAttribute("data-value") <= value
      );
    });
  }

  // Review Submission via AJAX
  reviewForm.addEventListener("submit", function (e) {
    e.preventDefault();
    let formData = new FormData(this);

    fetch(this.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCSRFToken(),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert(data.error);
        } else {
          reviewList.innerHTML += generateReviewHTML(data);
          reviewForm.reset();
          selectedRating = 0;
          highlightStars(0);
        }
      });
  });

  // Function to Generate Review HTML
  function generateReviewHTML(review) {
    return `
          <div id="review-${review.id}" class="review container mb-5">
              <strong>${review.user}</strong>
              <p>${generateStarHTML(review.rating)}</p>
              <p class="review-comment">${review.comment}</p>
              ${
                review.approved
                  ? ""
                  : "<span class='pending'>🫸 Pending Approval...</span>"
              }
              <button class="btn btn-success edit-review-btn" data-id="${
                review.id
              }">Edit</button>
              <button class="btn btn-danger delete-review-btn" data-id="${
                review.id
              }">Delete</button>
          </div>
      `;
  }

  // Function to Generate Star Icons
  function generateStarHTML(rating) {
    let starsHTML = "";
    for (let i = 1; i <= 5; i++) {
      starsHTML += `<span class="star ${
        i <= rating ? "selected" : ""
      }">★</span>`;
    }
    return starsHTML;
  }

  // Edit Review
  document.addEventListener("click", function (e) {
    if (e.target.classList.contains("edit-review-btn")) {
      let reviewDiv = e.target.closest(".review");
      let reviewId = e.target.dataset.id;
      let reviewComment =
        reviewDiv.querySelector(".review-comment").textContent;

      let newComment = prompt("Edit your review:", reviewComment);
      if (newComment) {
        fetch(`/cabins/review/${reviewId}/edit/`, {
          method: "POST",
          body: JSON.stringify({ comment: newComment }),
          headers: {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCSRFToken(),
          },
        })
          .then((response) => response.json())
          .then((data) => {
            reviewDiv.querySelector(".review-comment").textContent =
              data.comment;
            alert("✅ Review updated successfully!");
          });
      }
    }
  });



  // Delete Review
  document.addEventListener("click", function (e) {
    if (e.target.classList.contains("delete-review-btn")) {
      let reviewId = e.target.getAttribute("data-id");

      if (confirm("❌ Are you sure you want to delete this review?")) {
        fetch(`/cabins/review/${reviewId}/delete/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCSRFToken(),
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              e.target.closest(".review").remove();
              alert("🗑️ Review deleted successfully!");
            } else {
              alert("⚠️ Error deleting review.");
            }
          })
          .then(() => location.reload()); // Refresh after deleting
      }
    }
  });


  // Get CSRF Token
  function getCSRFToken() {
    let cookieValue = null;
    let cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith("csrftoken=")) {
        cookieValue = cookie.substring("csrftoken=".length);
        break;
      }
    }
    return cookieValue;
  }
});


