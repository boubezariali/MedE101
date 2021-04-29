// Handles rendering clinical features
import React, { useState } from 'react';
import { Dropdown, Form, Button } from "semantic-ui-react"

const options = [
    { key: "stroke", text: "Stroke", value: 'stroke' },
    { key: "cough", text: "Cough", value: 'cough' },
    {key: "fatigue", text: "Fatigue", value: 'fatigue' },
    { key: "chest_pain", text: "Chest pain", value: 'chest_pain' },
    { key: "fever", text: "Fever", value: "fever" },
    { key: "body_aches", text: "Body aches", value: "body_aches" },
    { key: "shortness_of_breath", text: "Shortness of breath", value: "shortness_of_breath" }
]

const genderOptions = [
    { key: 'm', text: "Male", value: 'male' },
    { key: 'f', text: "Female", value: 'female' }
]

export const FeatureSelector = ({ onNewFeatures }) => {
    const [features, setFeatures] = useState([]);
    return (
        <Form>
            <Form.Group widths='equal'>
                <Form.Input fluid label="Age"/>
                <Form.Select
                    fluid
                    label="Sex"
                    options={genderOptions}/>
            </Form.Group>
            <Form.Field>
                <label>Clinical Features</label>
                <Dropdown
                    placeholder='Input Clinical Feature'
                    fluid
                    search
                    selection
                    multiple
                    options={options}
                    onChange={
                        (event, data) => setFeatures(data.value)
                    }
                />
            </Form.Field>
            <Form.Field>
                <Button onClick={async () => {
                    const response = await fetch('/add_feature', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(features)
                    })

                    if (response.ok) {
                        console.log("response ok");
                        console.log(features);
                        onNewFeatures(features);
                    }
                }}
                >Submit</Button>
            </Form.Field>
        </Form>
    )
}