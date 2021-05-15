var charCNN_Results = String;
var YOLO_Results = [];

if (charCNN_Results === "Phishing" && YOLO_Results["Conf_Score"] > "0.7") {
    showMain_Results ("Phishing");
}

else if (YOLO_Results["Conf_Score"] > "0.7" && charCNN_Results === "valid") {
    checkDomain();
    showMain_Results("Suspicious");
}

else if (charCNN_Results === "Phishing") {
    showMain_Results ("Suspicious")
}

else {
    showMain_Results("Legitimate");
}
