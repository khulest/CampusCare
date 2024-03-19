// index.js

document.addEventListener("DOMContentLoaded", function() {
  var maintenanceLogs = document.querySelectorAll('.maintenance-log');
  maintenanceLogs.forEach(function(log) {
      log.addEventListener('click', function() {
          log.classList.toggle('active');
      });
  });
});
