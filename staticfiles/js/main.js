document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript užkrautas!");

    // Klausomės datos input lauko pasikeitimo
    const dateInput = document.getElementById("id_slot_date");
    if (dateInput) {
        dateInput.addEventListener("change", function() {
            let selectedDate = this.value;
            console.log("Pasirinkta data:", selectedDate);
            
            // Siunčiame AJAX užklausą, kad gautume laisvus laikus
            fetch(`/get_available_slots?date=${encodeURIComponent(selectedDate)}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Serverio klaida, prašome pabandyti dar kartą");
                    }
                    return response.json();
                })
                .then(data => {
                    const slotSelect = document.getElementById("id_available_slot");
                    if (!slotSelect) {
                        console.error("Nepavyko rasti laiko pasirinkimo elemento");
                        return;
                    }
                    // Išvalome ankstesnes parinktis
                    slotSelect.innerHTML = '';
                    
                    // Jei grąžinta klaida, rodome ją kaip parinktį
                    if (data.error) {
                        const errorOption = document.createElement('option');
                        errorOption.textContent = data.error;
                        slotSelect.appendChild(errorOption);
                    } else {
                        // Užpildome laiko parinkčių elementą gautais duomenimis
                        data.forEach(function(slot) {
                            const option = document.createElement('option');
                            option.value = slot.id;
                            option.textContent = slot.slot_time;
                            slotSelect.appendChild(option);
                        });
                    }
                })
                .catch(error => {
                    console.error("Klaida užklausoje:", error);
                });
        });
    }

    // Papildomos mygtukų paspaudimo funkcijos
    document.body.addEventListener("click", function(event) {
        if (event.target.matches(".btn-primary")) {
            console.log("Registracijos mygtukas paspaustas!");
        }
        if (event.target.matches(".btn-success")) {
            console.log("Rezervacijos mygtukas paspaustas!");
        }
    });
});




