import React, { useEffect, useState } from 'react';
import { Container } from 'semantic-ui-react';
import './App.css';
import { ClinicalFeatures } from './components/ClinicalFeatures';
import { FeatureSelector } from './components/FeatureSelector';


function App() {
  const [features, setFeatures] = useState([]);
  useEffect(() => {
    fetch('/tester').then(response =>
      response.json().then(data => {
        setFeatures(data.test_items);
      }));
  }, [])

  return (
    <div className="App">
      <Container style={{ marginTop: 40 }}>
        <FeatureSelector
          onNewFeature={
            feature => setFeatures(currentFeatures => [...currentFeatures, feature])
          } />
        <ClinicalFeatures features={features} />
      </Container>
    </div>
  );
}

export default App;
