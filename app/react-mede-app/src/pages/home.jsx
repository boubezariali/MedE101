/*home.jsx*/
import React from "react";
import { Container, Header, Button, Card } from 'semantic-ui-react';
import { Link } from "react-router-dom";

const MainPage = () => {
    return (
        <div>
            <Container style={{ marginTop: 40, marginBottom: 80 }}>
                <Card centered={true} fluid={true}>
                    <Card.Content header={"Welcome to IntelligentDDx!"}/>
                    <Card.Content>
                        <Card.Description>Enter either Game Mode or Diagnosis Mode</Card.Description>
                    </Card.Content>
                    <Card.Content extra>
                        <Button><Link to="/diagnosis">Diagnosis Mode</Link></Button>
                        <Button><Link to="/game">Game Mode</Link></Button>
                    </Card.Content>
                </Card>

            </Container>
        </div>
    );
};

export default MainPage;