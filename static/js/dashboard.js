var topicSelect = document.getElementById('dashboardTopicSelect');

topicSelect.onchange = function() {
    var selectedTopic = document.getElementById("dashboardTopicSelect").value;
    topicSections = document.getElementsByClassName("topic_row")
    for(var i = 0;i < topicSections.length;i++){
        if(selectedTopic == "all"){
            topicSections[i].classList.remove("dashboard_hidden_row")
        } else {
            if (topicSections[i].getElementsByTagName("h2")[0].innerText != selectedTopic){
                topicSections[i].classList.add("dashboard_hidden_row")
            } else {
                topicSections[i].classList.remove("dashboard_hidden_row")
            }
        }
    }
   
 }

 var onPageSearch = document.getElementById('dashboardOnPageSearchForm');
 onPageSearch.addEventListener("submit", function(e) {
    e.preventDefault()
    dashboardOnPageSearchTerm = document.getElementById('dashboardOnPageSearchTerm').value.toLowerCase();
    // Getting topic sections
    topicSections = document.getElementsByClassName("topic_row")
    // If search term is not empty
    if(dashboardOnPageSearchTerm !== ""){
        //Loop over top sections
        for(var i = 0;i < topicSections.length;i++){
            // hide all topic rows
            topicSections[i].classList.add("dashboard_hidden_row")
            //get all cpjects cards per topic, hide them
            projectCards = topicSections[i].getElementsByClassName("dashboardcard")
            for(var j = 0;j < projectCards.length;j++){
                projectCards[j].parentNode.classList.add("dashboard_hidden_card")
                // Get inner text and unhide if matches search
                projectTitle = projectCards[j].getElementsByTagName("h5")[0].innerText.toLowerCase()
                if(projectTitle.search(dashboardOnPageSearchTerm) !== -1 ){
                    topicSections[i].classList.remove("dashboard_hidden_row")
                    projectCards[j].parentNode.classList.remove("dashboard_hidden_card")
                } else {
                    // Otherwise loop over tasks and see if they match
                    taskTitles = projectCards[j].getElementsByClassName("dashboard_card_task_title_text")
                    for(var h = 0;h < taskTitles.length;h++){
                        if(taskTitles[h].innerText.toLowerCase().search(dashboardOnPageSearchTerm) !== -1){
                            topicSections[i].classList.remove("dashboard_hidden_row")
                            projectCards[j].parentNode.classList.remove("dashboard_hidden_card")
                            break
                        } 
                    }
                }
            }
        }
    // Else just unhide everything
    } else {
        for(var i = 0;i < topicSections.length;i++){
            topicSections[i].classList.remove("dashboard_hidden_row")
            projectCards = topicSections[i].getElementsByClassName("dashboardcard")
            for(var j = 0;j < projectCards.length;j++){
                projectCards[j].parentNode.classList.remove("dashboard_hidden_card")
            }
        }
    }
    
 })
