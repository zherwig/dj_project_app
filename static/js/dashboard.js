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
    // If search term is not empty loop over topics and projects, hide all,
    // the cards and topics then unhide those that match
    if(dashboardOnPageSearchTerm !== ""){
        for(var i = 0;i < topicSections.length;i++){
            topicSections[i].classList.add("dashboard_hidden_row")
            projectCards = topicSections[i].getElementsByClassName("dashboardcard")
            for(var j = 0;j < projectCards.length;j++){
                projectCards[j].parentNode.classList.add("dashboard_hidden_card")
                projectTitle = projectCards[j].getElementsByTagName("h5")[0].innerText.toLowerCase()
                if(projectTitle.search(dashboardOnPageSearchTerm) !== -1 ){
                    topicSections[i].classList.remove("dashboard_hidden_row")
                    projectCards[j].parentNode.classList.remove("dashboard_hidden_card")
                }
            }
        }
    // Else just unhide everything
    } else {
        for(var i = 0;i < topicSections.length;i++){
            topicSections[i].classList.remove("dashboard_hidden_row")
            projectCards = topicSections[i].getElementsByClassName("dashboardcard")
            for(var i = 0;i < projectCards.length;i++){
                projectCards[i].parentNode.classList.remove("dashboard_hidden_card")
            }
        }
    }
    
 })
