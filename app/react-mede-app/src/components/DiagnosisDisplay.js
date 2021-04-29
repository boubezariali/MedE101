import React, { useState } from 'react';
import { Container, Card } from "semantic-ui-react"

export const DiagnosisDisplay = ({ features }) => {
    // Fetch diagnosis from Python (features already send via POST request)
    const [diagnosis, setDiagnosis] = useState("");

    // Only display diagnosis if features have been submitted
    if (features.length <= 0) {
        return (<Container />);
    }

    fetch('/retrieve_diagnosis').then(response =>
        response.json().then(data => {
            setDiagnosis(data.diagnosis);
        }));

    return (
        <Container>
            <Card centered={true} fluid={true} style={{flex:1, backgroundColor:'#F8F8F8'}}>
                <Card.Content header={"Diagnosis Result:"} />
                <Card.Content>
                    The diagnosis is <b>{diagnosis}</b>.
                    For more information, visit the
                    <a href="https://www.merckmanuals.com/professional"> Merk Manual.</a>
                </Card.Content>
            </Card>
        </Container>
    )
}