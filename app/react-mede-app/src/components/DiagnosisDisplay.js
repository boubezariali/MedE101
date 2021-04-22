import React, { useState } from 'react';
import { Header, Container } from "semantic-ui-react"

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
            <Header as='h2' block={true} >
                <Header.Content>
                    Diagnosis Result:
                    <Header.Subheader>{diagnosis}</Header.Subheader>
                </Header.Content>
            </Header>
        </Container>
    )
}