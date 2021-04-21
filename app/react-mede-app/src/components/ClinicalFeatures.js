// Handles rendering clinical features
import React from 'react';
import { List, Header } from "semantic-ui-react"
export const ClinicalFeatures = ({ features }) => {
    return (
        <List>
            {features.map(feature => {
                return (
                    <List.Item key={feature}>
                        <Header>{feature}</Header>
                    </List.Item>
                )
            })}
        </List>
    )
}