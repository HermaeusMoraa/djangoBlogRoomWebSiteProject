document.addEventListener('DOMContentLoaded', function () {
    $(document).ready(function () {
        // Handle the like button click event
        $('#like-button').click(function () {
            handleLikeButtonClick($(this));
        });

        // Handle the save button click event
        $('#save-button').click(function () {
            handleSaveButtonClick($(this));
        });
    });

    /**
     * Handle like button click event.
     * @param {jQuery Object} button - The button that was clicked.
     */
    function handleLikeButtonClick(button) {
        var url = button.data('url');

        $.ajax({
            url: url,
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken()
            },
            success: function (response) {
                updateLikeButton(button, response.liked);
                updateLikeCount(response.like_count);
            },
            error: function () {
                alert('An error occurred. Please try again.');
            }
        });
    }

    /**
     * Handle save button click event.
     * @param {jQuery Object} button - The button that was clicked.
     */
    function handleSaveButtonClick(button) {
        var url = button.data('url');

        $.ajax({
            url: url,
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken()
            },
            success: function (response) {
                updateSaveButton(button, response.saved);
            },
            error: function () {
                alert('An error occurred. Please try again.');
            }
        });
    }

    /**
     * Update the like button based on the response.
     * @param {jQuery Object} button - The like button to update.
     * @param {boolean} liked - Whether the post is liked or not.
     */
    function updateLikeButton(button, liked) {
        if (liked) {
            button.html('<i class="fa-solid fa-thumbs-up"></i> Unlike');
        } else {
            button.html('<i class="fa-solid fa-thumbs-up"></i> Like');
        }
    }

    /**
     * Update the like count display.
     * @param {number} likeCount - The updated like count.
     */
    function updateLikeCount(likeCount) {
        $('#like-count').text(likeCount);
    }

    /**
     * Update the save button based on the response.
     * @param {jQuery Object} button - The save button to update.
     * @param {boolean} saved - Whether the post is saved or not.
     */
    function updateSaveButton(button, saved) {
        var saveText = saved ? 'Unsave' : 'Save';
        var iconColor = saved ? 'blue' : 'black';

        button.find('#save-text').text(saveText);
        button.find('i').removeClass('fa-bookmark').addClass('fa-bookmark').css('color', iconColor);
    }

    /**
     * Get the CSRF token from the page.
     * @returns {string} - The CSRF token.
     */
    function getCsrfToken() {
        return $('[name=csrfmiddlewaretoken]').val();
    }

});





