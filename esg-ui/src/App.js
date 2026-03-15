import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [file, setFile] = useState(null);
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const analyzeFile = async () => {

    if (!file) {
      alert("Upload a document first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );

      setReport(response.data);

      setLoading(false);

    } catch (error) {

      console.error(error);
      alert("Analysis failed");

      setLoading(false);
    }
  };

  return (

    <div className="container">

      <h1 className="title">AI ESG Risk Analyzer</h1>

      <div className="upload-box">

        <input type="file" onChange={handleFileChange} />

        <button onClick={analyzeFile}>
          Analyze ESG Report
        </button>

      </div>

      {loading && <p className="loading">Analyzing document...</p>}

      {report && (

        <div className="dashboard">

          <div className="card">
            <h3>Total Claims</h3>
            <p>{report.total_claims}</p>
          </div>

          <div className="card">
            <h3>Unverifiable Claims</h3>
            <p>{report.unverifiable_claims}</p>
          </div>

          <div className="card">
            <h3>No Evidence</h3>
            <p>{report.claims_without_evidence}</p>
          </div>

          <div className="card">
            <h3>Contradictions</h3>
            <p>{report.contradictions}</p>
          </div>

          <div className="risk-card">

            <h2>Risk Score</h2>

            <p className="risk-score">
              {report.risk_score}
            </p>

            <p className="risk-level">
              {report.risk_level}
            </p>

          </div>

        </div>

      )}

      {report && (

        <div className="claims">

          <h2>Flagged Claims</h2>

          {report.flagged_claims.map((item, index) => (

            <div key={index} className="claim-card">

              <p>{item.claim}</p>

              <span>
                {item.reason.join(", ")}
              </span>

            </div>

          ))}

        </div>

      )}

    </div>
  );
}

export default App;