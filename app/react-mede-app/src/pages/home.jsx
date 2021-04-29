/*home.jsx*/
import React from "react";
import { Container, Button, Card } from 'semantic-ui-react';
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
                        <Link to="/diagnosis"><Button>Diagnosis Mode</Button></Link>
                        <Link to="/game"><Button>Game Mode</Button></Link>
                    </Card.Content>
                </Card>

            </Container>
        </div>
    );
};

export default MainPage;